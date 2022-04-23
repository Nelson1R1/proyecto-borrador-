from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request,'app/index.html')

def tienda(request):
    return render(request,'app/tienda/Tiendaprincipal.html')

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