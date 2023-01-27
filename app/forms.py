from socket import fromshare
from django import forms
from .models import *

class PlantaForm(forms.ModelForm):
    class Meta:
        model = Planta
        fields = '__all__'
        
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
        'contraseña': forms.PasswordInput(),
    }
    
