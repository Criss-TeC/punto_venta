# tienda/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from tienda.forms import ProductoForm, VentaForm, VentaDetalleFormSet
from tienda.services import producto_service, venta_service
from tienda.models import Venta, VentaDetalle

def index(request):
    return render(request, 'tienda/index.html')

def lista_productos(request):
    productos = producto_service.listar_productos()
    return render(request, 'tienda/productos.html', {'productos': productos})

def detalle_producto(request, pk):
    producto = producto_service.obtener_producto(pk)
    return render(request, 'tienda/detalle_producto.html', {'producto': producto})

def nuevo_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto_service.crear_nuevo_producto(form.cleaned_data)
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'tienda/editar_producto.html', {'form': form})

def editar_producto(request, pk):
    producto = producto_service.obtener_producto(pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto_service.actualizar_producto_existente(pk, form.cleaned_data)
            return redirect('detalle_producto', pk=pk)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'tienda/editar_producto.html', {'form': form})

def eliminar_producto(request, pk):
    producto = producto_service.obtener_producto(pk)
    if request.method == "POST":
        producto_service.eliminar_producto_por_id(pk)
        return redirect('lista_productos')
    return render(request, 'tienda/eliminar_producto.html', {'producto': producto})

def lista_ventas(request):
    ventas = venta_service.listar_ventas()
    return render(request, 'tienda/ventas.html', {'ventas': ventas})

def nueva_venta(request):
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