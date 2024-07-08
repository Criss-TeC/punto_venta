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
    cantidad_vendida = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # Solo se ejecuta al crear una nueva venta
            self.producto.cantidad -= self.cantidad_vendida
            self.producto.save()
        super(Venta, self).save(*args, **kwargs)

    def __str__(self):
        return f"Venta de {self.cantidad_vendida} {self.producto.nombre}"