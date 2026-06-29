from django.shortcuts import render
from .models import Producto


def catalogo(request):
    productos = Producto.objects.filter(activo=True)

    contexto = {
        "productos": productos
    }

    return render(request, "tienda/catalogo.html", contexto)
