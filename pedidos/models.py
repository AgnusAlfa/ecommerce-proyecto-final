from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

from tienda.models import Producto


class Pedido(models.Model):

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    fecha = models.DateTimeField(
        auto_now_add=True
    )

    estado = models.CharField(
        max_length=50,
        default="Pendiente"
    )


    def total(self):

        return sum(
            item.subtotal()
            for item in self.items.all()
        )


    def __str__(self):

        return f"Pedido #{self.id} - {self.usuario.username}"



class ItemPedido(models.Model):

    pedido = models.ForeignKey(
        Pedido,
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

    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(0.01)
        ]
    )


    def subtotal(self):

        return self.precio * self.cantidad


    def __str__(self):

        return self.producto.nombre
    

