# tienda/models.py

from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Venta(models.Model):
<<<<<<< HEAD
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_vendida = models.IntegerField()
=======
>>>>>>> 6c037febb7494d48f150876fe8eecd596227bf87
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Venta - {self.fecha}'

class VentaDetalle(models.Model):
    venta = models.ForeignKey(Venta, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
<<<<<<< HEAD
        if not self.pk:  # Solo se ejecuta al crear una nueva venta
            self.producto.cantidad -= self.cantidad_vendida
            self.producto.save()
        super(Venta, self).save(*args, **kwargs)

    def __str__(self):
        return f"Venta de {self.cantidad_vendida} {self.producto.nombre}"
=======
        self.subtotal = self.producto.precio * self.cantidad
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.producto.nombre} - {self.cantidad}'
>>>>>>> 6c037febb7494d48f150876fe8eecd596227bf87
