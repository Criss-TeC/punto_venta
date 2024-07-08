# tienda/repositories/producto_repository.py

from tienda.models import Producto

def obtener_todos_los_productos():
    return Producto.objects.all()

def obtener_producto_por_id(producto_id):
    return Producto.objects.get(pk=producto_id)

def crear_producto(producto_data):
    return Producto.objects.create(**producto_data)

def actualizar_producto(producto, producto_data):
    for key, value in producto_data.items():
        setattr(producto, key, value)
    producto.save()
    return producto

def eliminar_producto(producto):
    producto.delete()
