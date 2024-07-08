# tienda/models.py

from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=0)
    fecha = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total = self.producto.precio * self.cantidad
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Venta de {self.producto.nombre} - {self.fecha}'
