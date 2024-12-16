from django import forms
from .models import Stock

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['titulo', 'tipo', 'prenda', 'talle', 'color', 'precio', 'stock']
