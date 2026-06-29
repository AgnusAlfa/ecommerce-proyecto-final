from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from tienda.models import Producto
from .models import Carrito, ItemCarrito

from pedidos.models import Pedido, ItemPedido



@login_required
def agregar_al_carrito(request, producto_id):

    producto = get_object_or_404(
        Producto,
        id=producto_id
    )

    if producto.stock <= 0:
        messages.error(
        request,
        "Producto sin stock."
    )
        return redirect("/")

    carrito, creado = Carrito.objects.get_or_create(
        usuario=request.user
    )

    item, creado = ItemCarrito.objects.get_or_create(
        carrito=carrito,
        producto=producto
    )

    if not creado:
        item.cantidad += 1
        item.save()

    messages.success(
        request,
        "Producto agregado al carrito."
    )

    return redirect("/")



@login_required
def ver_carrito(request):

    carrito, creado = Carrito.objects.get_or_create(
        usuario=request.user
    )

    return render(
        request,
        "carrito/carrito.html",
        {
            "carrito": carrito
        }
    )



@login_required
def actualizar_cantidad(request, item_id):

    item = get_object_or_404(
        ItemCarrito,
        id=item_id
    )

    cantidad = int(
        request.POST.get("cantidad", 1)
    )

    if cantidad > 0:

        item.cantidad = cantidad
        item.save()

        messages.success(
            request,
            "Cantidad actualizada correctamente."
        )

    return redirect("/carrito/")



@login_required
def eliminar_item(request, item_id):

    item = get_object_or_404(
        ItemCarrito,
        id=item_id
    )

    item.delete()

    messages.success(
        request,
        "Producto eliminado del carrito."
    )

    return redirect("/carrito/")



@login_required
def confirmar_compra(request):

    carrito = get_object_or_404(
        Carrito,
        usuario=request.user
    )


    if not carrito.items.exists():

        messages.error(
            request,
            "El carrito está vacío."
        )

        return redirect("/carrito/")


    pedido = Pedido.objects.create(
        usuario=request.user
    )


    for item in carrito.items.all():
        ItemPedido.objects.create(
        pedido=pedido,
        producto=item.producto,
        cantidad=item.cantidad,
        precio=item.producto.precio
    )

    item.producto.stock -= item.cantidad
    item.producto.save()


    carrito.items.all().delete()


    messages.success(
        request,
        "Compra realizada correctamente."
    )


    return redirect("/")
