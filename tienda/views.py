from django.shortcuts import render, get_object_or_404
from .models import Producto


def catalogo(request):
    productos = Producto.objects.filter(activo=True)

    contexto = {
        "productos": productos
    }

    return render(request, "tienda/catalogo.html", contexto)



def home(request):

    productos = Producto.objects.filter(
        activo=True
    )[:3]

    contexto = {
        "productos": productos
    }

    return render(
        request,
        "tienda/home.html",
        contexto
    )



def detalle_producto(request, producto_id):
    producto = get_object_or_404(
        Producto,
        id=producto_id,
        activo=True
    )

    contexto = {
        "producto": producto
    }

    return render(
        request,
        "tienda/detalle_producto.html",
        contexto
    )

