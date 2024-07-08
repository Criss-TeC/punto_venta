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