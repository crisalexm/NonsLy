from django.shortcuts import render
from django.http import HttpResponse
from gestionAcademica.models import Profesor
def login(request):

    return render(request,'login/login.html')

def buscar(request):
    
    if request.GeT["correo"]:
        #mensaje="Usuario encontrado: %r" %request.GET["correo"]
        correo=request.GET["correo"]
        
        profesor=Profesor.objects.filter(nombre__icontains=correo)
        
        return render
    else:
        mensaje = "No has introducido nada"
    
    return HttpResponse(mensaje)