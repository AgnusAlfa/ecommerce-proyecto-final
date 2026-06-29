from django.urls import path
from . import views


urlpatterns = [

    path(
        "agregar/<int:producto_id>/",
        views.agregar_al_carrito,
        name="agregar_carrito"
    ),

    path(
        "",
        views.ver_carrito,
        name="ver_carrito"
    ),

    path(
        "actualizar/<int:item_id>/",
        views.actualizar_cantidad,
        name="actualizar_cantidad"
    ),

    path(
        "eliminar/<int:item_id>/",
        views.eliminar_item,
        name="eliminar_item"
    ),

    path(
        "confirmar/",
        views.confirmar_compra,
        name="confirmar_compra"
    ),

]

