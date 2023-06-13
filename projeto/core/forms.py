from django import forms
from core.models import ProductModel, StockLineModel

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = "__all__"
        widgets = {
            'price': forms.TextInput(attrs={'type': 'str', 'step': '0.01'})
        }


class SaleProductForm(forms.ModelForm):
    class Meta:
        model = StockLineModel
        fields = ['stock','product','amount','balance']