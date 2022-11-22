from asyncio.windows_events import NULL
from contextlib import nullcontext
from gettext import NullTranslations
from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from datetime import datetime

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

def administrador(request):
    
    if request.GET["email"]:
        
       mensaje="Admin: %r" %request.GET["email"]
    
    else:
        mensaje="No has ingresado nada"
    
    return render(request,'admin/administrador.html')