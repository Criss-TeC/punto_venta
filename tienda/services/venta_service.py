
from tienda.repositories import venta_repository, producto_repository

def listar_ventas():
    return venta_repository.obtener_todas_las_ventas()

def crear_nueva_venta(venta_data):
    if venta_data['cantidad'] <= 0:
        raise ValueError("La cantidad debe ser mayor que 0.")

    producto = producto_repository.obtener_producto_por_id(venta_data['producto'].id)
    
    if producto.cantidad < venta_data['cantidad']:
        raise ValueError("No hay suficiente stock para realizar la venta.")
    
    producto.cantidad -= venta_data['cantidad']
    producto.save()
    
    return venta_repository.crear_venta(venta_data)
