# tienda/views.py

<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Venta
from .forms import ProductoForm, VentaForm
=======
from django.shortcuts import render, redirect
from django.contrib import messages
from tienda.forms import ProductoForm, VentaForm, VentaDetalleFormSet
from tienda.services import producto_service, venta_service
from tienda.models import Venta, VentaDetalle
>>>>>>> 6c037febb7494d48f150876fe8eecd596227bf87

def index(request):
    return render(request, 'tienda/index.html')

def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'tienda/lista_ventas.html', {'ventas': ventas})

def nueva_venta(request):
<<<<<<< HEAD
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
=======
    if request.method == "POST":
        venta_form = VentaForm(request.POST)
        detalle_formset = VentaDetalleFormSet(request.POST, instance=Venta())

        if venta_form.is_valid() and detalle_formset.is_valid():
            venta = venta_form.save()
            detalles = detalle_formset.save(commit=False)

            try:
                venta_service.crear_nueva_venta(venta, detalles)
                return redirect('lista_ventas')
            except ValueError as e:
                messages.error(request, str(e))
    else:
        venta_form = VentaForm()
        detalle_formset = VentaDetalleFormSet(instance=Venta())

    return render(request, 'tienda/nueva_venta.html', {
        'venta_form': venta_form,
        'detalle_formset': detalle_formset
    })
>>>>>>> 6c037febb7494d48f150876fe8eecd596227bf87
