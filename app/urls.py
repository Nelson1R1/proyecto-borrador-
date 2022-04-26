from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name='index'),
    path('tienda/', tienda, name='tienda'),
    path('nosotros/', nosotros, name='nosotros'),
    path('pago/', pago, name='pago'),
    path('registro/', registro, name='registro'),
    path('seguimiento/', seguimiento, name='seguimiento'),
    path('carrito/', carrito, name='carrito'),  
    path('donacion/', donacion, name='donacion'),     
    path('perfil/', perfil, name='perfil'),
    path('suscripcion/', suscribirse, name='suscripcion'),
    path('historial/', historial, name='historial'),
    path('ventas/', ventas, name='ventas')
]   