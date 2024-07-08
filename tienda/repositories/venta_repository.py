# tienda/repositories/venta_repository.py

from tienda.models import Venta

def obtener_todas_las_ventas():
    return Venta.objects.all()

def crear_venta(venta_data):
    return Venta.objects.create(**venta_data)
