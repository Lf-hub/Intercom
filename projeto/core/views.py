from typing import Any
from django.forms.models import BaseModelForm
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, CreateView
from core.models import StockModel, ProductModel
from core.forms import CreateProductForm

class IndexView(ListView):
    """
    Tela inicial de Produtos
    """
    model = ProductModel
    template_name = 'index.html'


class CreateProduct(CreateView):
    model = ProductModel
    template_name = 'create_product.html'
    form_class = CreateProductForm
    success_url = '/products/'

    def get_form(self):
        return CreateProductForm(self.request.POST)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.object = form.save()
            messages.add_message(request, messages.INFO, 'Salvo com sucesso!')
        else:
            messages.add_message(request, messages.ERROR, 'Error ao salvar o produto!')
        return redirect("core:create_product")