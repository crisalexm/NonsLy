from asyncio.windows_events import NULL
from contextlib import nullcontext
from gettext import NullTranslations
from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from datetime import datetime
""" from models """
#-----------------WEBSITE /------------------------------------

def index(request):
    
    return render(request,'index.html')

def login(request):

    return render(request,'login/login.html')

def soporte(request):
    
    return render(request,'soporte/soporte.html')

def faq(request):
    
    return render(request,'faq/faq.html')

def whoweare(request):
    
    return render(request,'whoweare/devs.html')

def demo(request):
    
    return render(request,'demo/demo.html')

#-----------------WEBSITE /------------------------------------


#-----------------CONFIGURACIÓN ACADEMICA ------------------------------------


def configuracion_periodo(request):
    
    return render(request,'configuracion_academica/periodo.html')

def configuracion_nivel(request):
    
    return render(request,'configuracion_academica/nivel.html')

def configuracion_curso(request):
    
    return render(request,'configuracion_academica/curso.html')
    
def configuracion_asignatura(request):

    return render(request,'configuracion_academica/asignatura.html')

#-----------------CONFIGURACIÓN ACADEMICA /------------------------------------


#-----------------CONFIGURACIÓN DE USUARIOS------------------------------------
def administracion(request):
    #profesor= Administracion.object.sall()
    #data={}
    return render(request,'configuracion_usuarios/administracion.html')

def administracion_profesor(request):
    
    return render(request,'configuracion_usuarios/profesor.html')

def administracion_alumno(request):
    
    return render(request,'configuracion_usuarios/alumno.html')

def administracion_apoderado(request):
    
    return render(request,'configuracion_usuarios/apoderado.html')


#-----------------CONFIGURACIÓN DE USUARIOS /------------------------------------


#-----------------CONFIGURACIÓN DE COLEGIO------------------------------------

def configuracion_colegio(request):
    
    return render(request, 'configuracion_colegio/colegio.html')

#-----------------CONFIGURACIÓN DE COLEGIO------------------------------------

