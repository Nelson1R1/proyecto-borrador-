from django.shortcuts import render

# Create your views here.

from .models import *
from .forms import *

def index(request):
    return render(request,'app/index.html')

#SECCION AGREGAR PRODUCTO
def agregarpr(request):
    datos = {
        'form' : Productoform()
    }
    if request.method == 'POST' :
        formulario = Productoform (request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje']="Prodcuto agregado correctamente"


    return render(request,'app/agregarpr/agregarpr.html')





def tienda(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }

    return render(request,'app/tienda/Tiendaprincipal.html',datos)

def nosotros(request):
    return render(request,'app/nosotros/nosotros.html')

def pago(request):
    return render(request,'app/pago/pago.html')

def carrito(request):
    return render(request,'app/pago/carrito.html')

def donacion(request):
    return render(request,'app/donacion/suspago.html')

def registro(request):
    return render(request,'app/registrarse/registrarse.html')

def seguimiento(request):
    return render(request,'app/seguimiento/seguimiento.html')

def perfil(request):
    return render(request,'app/perfil/perfil.html')

def suscribirse(request):
    return render(request, 'app/suscripcion/suscripcion.html')

def historial(request):
    return render(request,'app/historial/historial.html')

def ventas(request):
    return render(request, 'app/ventas/ventas.html')

def agregarProducto(request):
    datos = {
        'form': Productoform()
    }
    if request.method == 'POST' :
        formulario = Productoform(request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save
            datos['mensaje'] = "Producto agregado de forma correcta."
    return render (request, 'app/agregarpr/agregarpr.html', datos)