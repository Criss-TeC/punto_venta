# Generated by Django 5.0.6 on 2024-07-08 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_remove_venta_cantidad_remove_venta_producto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='total',
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='ventadetalle',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
