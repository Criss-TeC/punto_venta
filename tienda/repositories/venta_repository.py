# tienda/repositories/venta_repository.py

from tienda.models import Venta

def obtener_todas_las_ventas():
    return Venta.objects.all()

def crear_venta(venta):
    venta.save()
    return venta
