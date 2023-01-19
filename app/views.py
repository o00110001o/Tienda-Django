from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def api(request):
    return render(request,'api.html')

def carrito(request):
    return render(request,'carrito.html')

def contacto(request):
    return render(request,'contacto.html')

def estadopedido(request):
    return render(request,'estadopedido.html')

def estadopedidoadmin(request):
    return render(request,'estadopedidoadmin.html')

def estadopedidousuario(request):
    return render(request,'estadopedidousuario.html')

def formulario(request):
    return render(request,'formulario.html')

def formularioSuscripcion(request):
    return render(request,'formularioSuscripcion.html')

def index_formualrioSuscripcion(request):
    return render(request,'index_formualrioSuscripcion.html')

def index_user(request):
    return render(request,'index_user.html')

def login(request):
    return render(request,'login.html')

def productos(request):
    return render(request,'productos.html')

def registration(request):
    return render(request,'registration.html')

def suscripcion(request):
    return render(request,'suscripcion.html')

def terminos_condiciones(request):
    return render(request,'terminos_condiciones.html')

#CRUD PLANTAS