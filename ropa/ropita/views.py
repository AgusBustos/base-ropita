from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import StockForm
from .models import Stock
from django.shortcuts import get_object_or_404



def index(request):
    return render(request,'index.html')

def ABM_Stock(request):
    return render(request,'ABM_s.html')

def lista_stock(request):
    stocks = Stock.objects.all()
    return render(request, 'lista_stock.html', {'stocks': stocks})

def editar_stock(request, pk):
    stock = get_object_or_404(Stock, pk=pk)  # Obtener el producto a editar por su ID (pk)
    
    if request.method == 'POST':
        form = StockForm(request.POST, instance=stock)  # Pasar la instancia del producto para editar
        if form.is_valid():
            form.save()  # Guardar los cambios
            return redirect('lista_stock')  # Redirigir a la lista de stock
    else:
        form = StockForm(instance=stock)  # Crear un formulario con los datos actuales del producto
    
    return render(request, 'editar_stock.html', {'form': form, 'stock': stock})

def eliminar_stock(request, id):
    stock = get_object_or_404(Stock, id=id)
    stock.delete()
    return redirect('lista_stock')

def crear_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el formulario en la base de datos
            return redirect('lista_stock')  # Redirige a la lista de stock
    else:
        form = StockForm()  # Si no es POST, renderiza un formulario vacío
    
    return render(request, 'ABM_s.html', {'form': form})
