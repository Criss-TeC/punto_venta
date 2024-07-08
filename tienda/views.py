# tienda/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Venta
from .forms import ProductoForm, VentaForm

def index(request):
    return render(request, 'tienda/index.html')

def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'tienda/lista_ventas.html', {'ventas': ventas})

def nueva_venta(request):
    productos = Producto.objects.all()
    if request.method == 'POST':
        venta_form = VentaForm(request.POST)
        if venta_form.is_valid():
            venta_form.save()
            return redirect('lista_ventas')
    else:
        venta_form = VentaForm()

    return render(request, 'tienda/nueva_venta.html', {'venta_form': venta_form, 'productos': productos})

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/lista_productos.html', {'productos': productos})

def nuevo_producto(request):
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST)
        if producto_form.is_valid():
            producto_form.save()
            return redirect('lista_productos')
    else:
        producto_form = ProductoForm()

    return render(request, 'tienda/nuevo_producto.html', {'producto_form': producto_form})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'tienda/detalle_producto.html', {'producto': producto})

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST, instance=producto)
        if producto_form.is_valid():
            producto_form.save()
            return redirect('lista_productos')
    else:
        producto_form = ProductoForm(instance=producto)

    return render(request, 'tienda/editar_producto.html', {'producto_form': producto_form})