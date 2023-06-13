from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from core.models import ProductModel, StockLineModel
from core.forms import CreateProductForm, SaleProductForm

class IndexView(ListView):
    model = ProductModel
    template_name = 'index.html'


class CreateProduct(CreateView):
    model = ProductModel
    template_name = 'create_product.html'
    form_class = CreateProductForm

    def get_form(self):
        return CreateProductForm(self.request.POST)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.object = form.save()
            messages.add_message(request, messages.INFO, 'Salvo com sucesso!')
        else:
            messages.add_message(request, messages.ERROR, 'Error ao salvar o produto!')
        return redirect("core:index")


class DetailProductView(DetailView):
    model = ProductModel
    template_name = 'detail_product.html'


class UpdateProductView(UpdateView):
    model = ProductModel
    template_name = 'edit_product.html'
    form_class = CreateProductForm

    def post(self, request, *args, **kwargs):
        price = self.request.POST.get('price').replace(',','.')
        if self.request.POST.get('stock_mini'):
            mini = int(self.request.POST.get('stock_mini'))
        else:
            mini = 0
        data = {
            "product":self.request.POST.get('product'),
            "price":float(price),
            "stock_current":self.request.POST.get('stock_current'),
            "product_type":self.request.POST.get('product_type'),
            "produtc_vol":self.request.POST.get('produtc_vol'),
            "stock_mini": mini
        }
        obj, created = ProductModel.objects.update_or_create(
                                product=self.request.POST.get('product'),
                                defaults=data
                            )
        return redirect("core:index")

class DeleteProductView(DeleteView):
    model = ProductModel
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect("core:index")

class SaleProduct(CreateView):
    model = StockLineModel
    template_name = 'sale_product.html'
    form_class = SaleProductForm