from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

from tienda.models import Producto


class Carrito(models.Model):

    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    creado = models.DateTimeField(
        auto_now_add=True
    )


    def total(self):

        return sum(
            item.subtotal()
            for item in self.items.all()
        )


    def __str__(self):

        return f"Carrito de {self.usuario.username}"



class ItemCarrito(models.Model):

    carrito = models.ForeignKey(
        Carrito,
        related_name="items",
        on_delete=models.CASCADE
    )

    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE
    )

    cantidad = models.PositiveIntegerField(
        default=1,
        validators=[
            MinValueValidator(1)
        ]
    )


    def subtotal(self):

        return self.producto.precio * self.cantidad


    def __str__(self):

        return self.producto.nombre
    
