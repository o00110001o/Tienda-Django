from django.shortcuts import render, redirect
from app.forms import PlantaForm, UsuarioForm
from .models import Planta, Usuario

# Create your views here.
def index(request):
    return render(request,'index.html')


#CRUD PLANTAS

# SECCION LISTAR
def listarPlantas(request):
    plantas = Planta.objects.all()
    datos={
        'plantas' : plantas
    }
    
    return render(request, 'Crud_Plantas/listarPlantas.html', datos)


# SECCION CREAR
def crearPlantas(request):
    datos = {
        'form' : PlantaForm()
    }

    if request.method == 'POST':
        formulario = PlantaForm(request.POST, files=request.FILES)
        
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Guardados correctamente"
    
    return render(request, 'Crud_Plantas/crearPlantas.html', datos)


# SECCION MODIFICAR
def modificarPlantas(request, id):
    
    planta = Planta.objects.get(id=id)
    datos = {
        'form' : PlantaForm(instance=planta)
    }
    if request.method == 'POST':
        formulario = PlantaForm(request.POST, instance=planta)
        
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Producto modificado correctamente!'

    return render(request, 'Crud_Plantas/modificarPlantas.html', datos)

# SECCION ELIMINAR
def eliminarPlantas (request, id):

    planta = Planta.objects.get(id=id)

    planta.delete()

    return redirect (to="../listarPlantas")

#-------------------------------------------------------------------------------------------------------------------------------------------

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
    plantas = Planta.objects.all()
    datos={
        'plantas' : plantas
    }
    
    return render(request,'productos.html', datos)

def registration(request):
    datos = {
        'form' : UsuarioForm()
    }

    if request.method == 'POST':
        formulario = UsuarioForm(request.POST, files=request.FILES)
        
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Uuario registrado correctamente"
    
    return render(request,'registration.html' , datos)

def suscripcion(request):
    return render(request,'suscripcion.html')

def terminos_condiciones(request):
    return render(request,'terminos_condiciones.html')