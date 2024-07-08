
from tienda.repositories import venta_repository, producto_repository


def listar_ventas():
    return venta_repository.obtener_todas_las_ventas()

def crear_nueva_venta(venta, detalles):
    total = 0
    for detalle in detalles:
        if detalle.cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0.")

        producto = detalle.producto
        if producto.cantidad < detalle.cantidad:
            raise ValueError(f"No hay suficiente stock para {producto.nombre}.")
        
        producto.cantidad -= detalle.cantidad
        producto.save()

        detalle.venta = venta
        detalle.save()
        total += detalle.subtotal
    
    venta.total = total
    venta.save()
    return venta