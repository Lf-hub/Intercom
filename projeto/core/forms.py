from django import forms
from core.models import ProductModel

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = "__all__"
        widgets = {
            'price': forms.TextInput(attrs={'type': 'number', 'step': '0.01'})
        }
    
    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("O preço deve ser maior que zero.")
        return price