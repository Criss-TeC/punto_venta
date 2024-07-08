# tienda/forms.py
from django import forms
from tienda.models import Producto, Venta, VentaDetalle
from django.forms import inlineformset_factory


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'cantidad']

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
<<<<<<< HEAD
        fields = ['producto', 'cantidad_vendida']

    def clean_cantidad_vendida(self):
        cantidad_vendida = self.cleaned_data['cantidad_vendida']
        producto = self.cleaned_data['producto']
        if cantidad_vendida <= 0:
            raise forms.ValidationError('La cantidad vendida debe ser mayor que cero.')
        if cantidad_vendida > producto.cantidad:
            raise forms.ValidationError('La cantidad vendida no puede ser mayor que la cantidad disponible en el inventario.')
        return cantidad_vendida
=======
        fields = []

class VentaDetalleForm(forms.ModelForm):
    class Meta:
        model = VentaDetalle
        fields = ['producto', 'cantidad']

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad <= 0:
            raise forms.ValidationError("La cantidad debe ser mayor que 0.")
        return cantidad

VentaDetalleFormSet = inlineformset_factory(Venta, VentaDetalle, form=VentaDetalleForm, extra=1, can_delete=True)
>>>>>>> 6c037febb7494d48f150876fe8eecd596227bf87
