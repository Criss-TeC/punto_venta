# tienda/forms.py
from django import forms
from tienda.models import Producto, Venta

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'cantidad']

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['producto', 'cantidad_vendida']

    def clean_cantidad_vendida(self):
        cantidad_vendida = self.cleaned_data['cantidad_vendida']
        producto = self.cleaned_data['producto']
        if cantidad_vendida <= 0:
            raise forms.ValidationError('La cantidad vendida debe ser mayor que cero.')
        if cantidad_vendida > producto.cantidad:
            raise forms.ValidationError('La cantidad vendida no puede ser mayor que la cantidad disponible en el inventario.')
        return cantidad_vendida