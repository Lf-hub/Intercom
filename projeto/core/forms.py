from django import forms
from core.models import ProductModel

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = "__all__"
