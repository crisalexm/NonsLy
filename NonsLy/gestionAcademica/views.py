from django.shortcuts import render, redirect

# Create your views here.
from asyncio.windows_events import NULL
from contextlib import nullcontext
from gettext import NullTranslations
from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render, redirect
from datetime import datetime
from gestionAcademica.models import *
from ast import Delete
from django.http import JsonResponse
""" from models """

#-----------------CONFIGURACIÓN ACADEMICA ------------------------------------


def configuracion_periodo(request):
    
    return render(request,'gestionAcademica/configuracion_academica/periodo.html')


def configuracion_nivel(request):
    niveles = Nivel.objects.all()
    
    return render(request,'gestionAcademica/configuracion_academica/nivel.html', {"niveles": niveles})


def registra_nivel(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        curso = Nivel.objects.create(
            nombre = nombre,
        )
        return redirect('configuracion_nivel')  


def eliminar_nivel(self, niv_id):
    nivel= Nivel.objects.filter(niv_id=niv_id).delete()
    if len(nivel)>0:
        datos={'message':"Success"}
    else:
        datos={"message":"Alumno not found"}
    
    return redirect('configuracion_nivel')  

def configuracion_curso(request):
    
    cursos = Curso.objects.all()
    niveles = Nivel.objects.all()
    return render(request,'gestionAcademica/configuracion_academica/curso.html', {
        "cursos": cursos,
        "niveles": niveles
        })

def registra_curso(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        capacidad = request.POST.get('capacidad')
        annio_academico= request.POST.get('annio_academico')
        id_nivel= request.POST.get('nivel')
        nivel=Nivel.objects.get(niv_id=id_nivel)
        curso = Curso.objects.create(
            nombre = nombre,
            capacidad = capacidad,
            annio_academico = annio_academico,
            nivel=nivel
        )
        
        return redirect('configuracion_curso')  
    
def eliminar_curso(self, curso_id):
    curso= Curso.objects.filter(curso_id=curso_id).delete()
    if len(curso)>0:
        datos={'message':"Success"}
    else:
        datos={"message":"Alumno not found"}
    
    return redirect('configuracion_curso')  
    
    
def configuracion_asignatura(request):

    asignaturas = Asignatura.objects.all()


    return render(request,'gestionAcademica/configuracion_academica/asignatura.html', {
        "asignaturas": asignaturas,
        "cursos" : Curso.objects.all()
        })

def registra_asignatura(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        codigo = request.POST.get('codigo')
        id_curso = request.POST.get('curso')
        curso = Curso.objects.get(curso_id=id_curso)
        asignatura = Asignatura.objects.create(
            nombre = nombre,
            codigo= codigo, 
            curso = curso
        )
        
        return redirect('configuracion_asignatura')  
    
def eliminar_asignatura(self, asig_id):
    asignatura= Asignatura.objects.filter(asig_id=asig_id).delete()
    if len(asignatura)>0:
        datos={'message':"Success"}
    else:
        datos={"message":"Alumno not found"}
    
    return redirect('configuracion_asignatura')  

def administracion(request):
    
    
    return render(request,'gestionAcademica/configuracion_usuarios/administracion.html')

def administracion_profesor(request):
    
    profesores=Profesor.objects.all()
    
    
    return render(request,'gestionAcademica/configuracion_usuarios/profesor.html', {"profesores": profesores, "colegios":Colegio.objects.all()})

def registra_profesor(request):
    if request.method == "POST":
            
        nombre = request.POST.get('nombre')
        apellido1 = request.POST.get('apellido1')
        apellido2 = request.POST.get('apellido2')
        rut = request.POST.get('rut')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        genero= request.POST.get('genero')
        especialidad =request.POST.get('especialidad')
        colegio_nombres = [x.nombre for x in Colegio.objects.all()]
        colegio_ids = []
        for x in colegio_nombres:
            colegio_ids.append(int(request.POST.get(x)))
        profesor = Profesor.objects.create(nombre=nombre, 
                                           apellido1 = apellido1, 
                                           apellido2 = apellido2, 
                                           rut = rut,
                                           fecha_nacimiento = fecha_nacimiento, 
                                           email = email, 
                                           telefono = telefono, 
                                           genero = genero, 
                                           especialidad = especialidad)
        for x in colegio_ids:
            profesor.colegio.add(Colegio.objects.get(col_id=x))
        return redirect('administracion_profesor')
    
def eliminar_profesor(self, prof_id):
    profesor= Profesor.objects.filter(prof_id=prof_id).delete()
    if len(profesor)>0:
        datos={'message':"Success"}
    else:
        datos={"message":"Alumno not found"}
    
    return redirect('administracion_profesor')

def administracion_alumno(request):

    alumnos=Alumno.objects.all()
    
    return render(request,'gestionAcademica/configuracion_usuarios/alumno.html',
                  {
                      "alumnos": alumnos,
                      "cursos": Curso.objects.all(),
                      "colegios": Colegio.objects.all()
                      })

def registra_alumno(request):
    if request.method == "POST":
            
        nombre = request.POST.get('nombre')
        apellido1 = request.POST.get('apellido1')
        apellido2 = request.POST.get('apellido2')
        rut = request.POST.get('rut')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        genero= request.POST.get('genero')
        status= request.POST.get('status')
        id_curso = request.POST.get('curso')
        id_colegio = request.POST.get('colegio')
        colegio = Colegio.objects.get(col_id= id_colegio)
        curso = Curso.objects.get(curso_id=id_curso)
        alumno = Alumno.objects.create(nombre=nombre, 
                                       apellido1=apellido1, 
                                       apellido2=apellido2, 
                                       rut=rut,
                                       fecha_nacimiento=fecha_nacimiento, 
                                       email = email, 
                                       telefono = telefono, 
                                       genero=genero, 
                                       status=status,
                                       curso=curso,
                                       colegio = colegio
                                       )
        return redirect('administracion_alumno')
    
def eliminar_alumno(self, alum_id):
    alumno= Alumno.objects.filter(alum_id=alum_id).delete()
    if len(alumno)>0:
        datos={'message':"Success"}
    else:
        datos={"message":"Alumno not found"}
    
    return redirect('administracion_alumno')



def administracion_apoderado(request):
    
    apoderados=Apoderado.objects.all()
    
    return render(request,'gestionAcademica/configuracion_usuarios/apoderado.html', {"apoderados": apoderados, "alumnos":Alumno.objects.all()})

def registra_apoderado(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        apellido1 = request.POST.get('apellido1')
        apellido2 = request.POST.get('apellido2')
        rut = request.POST.get('rut')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        genero= request.POST.get('genero')
        alumno_nombres = [x.nombre for x in Alumno.objects.all()]
        alumno_ids = []
        for x in alumno_nombres:
            alumno_ids.append(int(request.POST.get(x)))

        apoderado = Apoderado.objects.create(nombre=nombre, 
                                            apellido1=apellido1, 
                                            apellido2=apellido2, 
                                            rut=rut,
                                            fecha_nacimiento=fecha_nacimiento, 
                                            email = email, 
                                            telefono = telefono, 
                                            genero=genero
                                       )
        for x in alumno_ids:
            apoderado.alumno.add(Alumno.objects.get(alum_id=x))
        return redirect('administracion_apoderado')
        
def eliminar_apoderado(self, apo_id):
    
    profesor= Profesor.objects.filter(apo_id=apo_id).delete()
    
    if len(profesor)>0:
        datos={'message':"Success"}
    else:
        datos={"message":"Alumno not found"}
    
    return redirect('administracion_apoderado')

#-----------------CONFIGURACIÓN DE USUARIOS /------------------------------------


#-----------------CONFIGURACIÓN DE COLEGIO------------------------------------

def configuracion_colegio(request):
    
    if request.method =="POST":
        nombre = request.POST.get("nombre")
        rbd = request.POST.get("rbd")
        sigla= request.POST.get("sigla")
        direccion= request.POST.get("direccion")
        colegio = Colegio.objects.create(
            nombre=nombre,
            rbd =rbd,
            sigla=sigla,
            direccion=direccion
        )
    
    return render(request, 'gestionAcademica/configuracion_colegio/colegio.html' )

#-----------------CONFIGURACIÓN DE COLEGIO------------------------------------

