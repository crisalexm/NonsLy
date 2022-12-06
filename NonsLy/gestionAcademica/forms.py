from django import forms 
from .models import Colegio
from datetime import datetime

class AdministracionForm(forms.Form):
    rut = forms.CharField(max_length=10, required=True)
    nombre = forms.CharField(max_length=50, required=True)
    apellido1 = forms.CharField(max_length=50, required=True)
    apellido2 = forms.CharField(max_length=50)
    fechanacimiento = forms.DateField(required=True)  # Field name made lowercase.
    telefono = forms.CharField(max_length=11, required=True)
    email = forms.EmailField(required=True)
    genero = forms.CharField(max_length=10, required=True)
    especialidad = forms.CharField(max_length=50,required=True)
    
    colegio=forms.ModelChoiceField(queryset=Colegio.objects.all())
    
    created_at = forms.DateTimeField(required=True)
    updated_at = forms.DateTimeField(required=True)