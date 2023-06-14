from django import forms
from core.models import ProductModel, StockLineModel, StockModel

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = "__all__"
        widgets = {
            'price': forms.TextInput(attrs={'type': 'str', 'step': '0.01'})
        }


class StockProductForm(forms.ModelForm):
    class Meta:
        model = StockModel
        fields = "__all__"


class StockLineProductForm(forms.ModelForm):
    class Meta:
        model = StockLineModel
        fields = ['stock','product','amount','balance']