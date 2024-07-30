from django.forms import ModelForm

from django import forms
from .models import Sale
from .models import Product

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'
        labels = {
            'product': 'Jina la bidhaa',
            'quantity_sold': 'Idadi iliyouzwa',
            'selling_price': 'Bei ya kuuza',
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'name': 'Jina la bidhaa',
            'description': 'Maelezo',
            'cost_price': 'Bei ya kununua',
            'selling_price': 'Bei ya kuuza',
            'quantity': 'Idadi ilionunuliwa',
        }

class ExistingProductForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), label='Chagua bidhaa')
    quantity = forms.IntegerField(min_value=1, label='Idadi')
