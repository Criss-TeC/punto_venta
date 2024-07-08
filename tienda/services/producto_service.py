# tienda/services/producto_service.py

from tienda.repositories import producto_repository

def listar_productos():
    return producto_repository.obtener_todos_los_productos()

def obtener_producto(producto_id):
    return producto_repository.obtener_producto_por_id(producto_id)

def crear_nuevo_producto(producto_data):
    return producto_repository.crear_producto(producto_data)

def actualizar_producto_existente(producto_id, producto_data):
    producto = producto_repository.obtener_producto_por_id(producto_id)
    return producto_repository.actualizar_producto(producto, producto_data)

def eliminar_producto_por_id(producto_id):
    producto = producto_repository.obtener_producto_por_id(producto_id)
    producto_repository.eliminar_producto(producto)
