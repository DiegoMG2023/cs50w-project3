from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("registrarse",views.registro, name="registro"),
    path("menu",views.menu, name="menu"),
    path("detalles_pizza", views.detalles_pizza, name="detalles_pizza"),
]
