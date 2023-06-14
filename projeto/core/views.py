from django.shortcuts import redirect, resolve_url, render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from core.models import ProductModel, StockLineModel, StockModel
from core.forms import CreateProductForm, StockLineProductForm, StockProductForm

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

def SaleProduct(request):
    model = StockLineModel
    template_name = 'sale_product.html'
    stock_form = StockModel()
    item_stock_formset = inlineformset_factory(
        StockModel,
        StockLineModel,
        form=StockLineProductForm,
        extra=0,
        min_num=1,
        validate_min=True,
    )
    if request.method == 'POST':
        form = StockProductForm(request.POST, instance=stock_form, prefix='main')
        formset = item_stock_formset(request.POST,instance=stock_form, prefix='estoque')
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            url = 'core:index'
            return HttpResponseRedirect(resolve_url(url))
    else:
        form = StockProductForm(instance=stock_form, prefix='main')
        formset = item_stock_formset(instance=stock_form, prefix='estoque')
    
    context = {'form':form, 'formset':formset}
    return render(request, template_name, context) 