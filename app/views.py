from django.shortcuts import render, redirect
from app.forms import PlantaForm
from .models import Planta

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
    
    return render(request, 'listarPlantas.html', datos)


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
    
    return render(request, 'crearPlantas.html', datos)


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

    return render(request, 'modificarPlantas.html', datos)

# SECCION ELIMINAR
def eliminarPlantas (request, id):

    planta = Planta.objects.get(id=id)

    planta.delete()

    return redirect (to="../listarPlantas")