from django.shortcuts import render, redirect

# Create your views here.
from asyncio.windows_events import NULL
from contextlib import nullcontext
from gettext import NullTranslations
from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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
        nivel = Nivel.objects.create(
            nombre = nombre,
        )
        return redirect('configuracion_nivel')  

def edicion_nivel(request, niv_id):
    nivel = Nivel.objects.filter(niv_id=niv_id).first()
    return render (request, 'gestionAcademica/configuracion_academica/edicion_nivel.html', {"nivel": nivel})
    
def editar_nivel(request):
    nombre = request.POST.get('nombre')
    id = int(request.POST.get('id'))
    nivel = Nivel.objects.get(niv_id=id) 
    nivel.nombre = nombre
    nivel.save()
    return redirect ("configuracion_nivel")


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
 
def edicion_curso(request, curso_id):
    curso = Curso.objects.filter(curso_id=curso_id).first()
    niveles = Nivel.objects.all()
    return render (request, 'gestionAcademica/configuracion_academica/edicion_curso.html', {"curso": curso, "niveles":niveles}) 

def editar_curso(request):
    id = int(request.POST.get('id'))
    id_nivel= request.POST.get('nivel')
    nombre = request.POST.get('nombre')
    capacidad = request.POST.get('capacidad')
    annio_academico = request.POST.get('annio_academico')
    
    nivel=Nivel.objects.get(niv_id=id_nivel)
    curso = Curso.objects.get(curso_id=id) 
    
    curso.nombre = nombre
    curso.capacidad = capacidad
    curso.annio_academico = annio_academico
    curso.nivel= nivel
    curso.save()
    return redirect ("configuracion_curso")
     
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

def edicion_asignatura(request,asig_id): 
    asignatura = Asignatura.objects.filter(asig_id=asig_id).first()
    cursos = Curso.objects.all()
    return render (request, 'gestionAcademica/configuracion_academica/edicion_asignatura.html', {"asignatura": asignatura, "cursos":cursos}) 

def editar_asignatura(request):
    nombre = request.POST.get('nombre')
    codigo = request.POST.get('codigo')
    id = int(request.POST.get('id'))
    id_curso= request.POST.get('curso')
    curso = Curso.objects.get(curso_id=id_curso)
    asignatura = Asignatura.objects.get(asig_id=id) 
    asignatura.nombre = nombre
    asignatura.codigo = codigo
    asignatura.curso= curso
    asignatura.save()
    return redirect ("configuracion_asignatura")

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

def edicion_profesor(request, prof_id):
    profesor = Profesor.objects.filter(prof_id=prof_id).first()
    
    return render(request,'gestionAcademica/configuracion_usuarios/edicion_profesor.html',
                  {
                      "profesor" : profesor,
                      "colegios":Colegio.objects.all()
                  })

def editar_profesor(request):
        id = int(request.POST.get('id'))
        nombre = request.POST.get('nombre')
        apellido1 = request.POST.get('apellido1')
        apellido2 = request.POST.get('apellido2')
        rut = request.POST.get('rut')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        genero= request.POST.get('genero')
        especialidad =request.POST.get('especialidad')
        profesor = Profesor.objects.get(prof_id=id) 
        colegio_nombres = [x.nombre for x in Colegio.objects.all()]
        colegio_ids = []
        
        for x in colegio_nombres:
            colegio_ids.append(str(request.POST.get(x)))
        
        for x in colegio_ids:
            profesor.colegio.add(Colegio.objects.get(col_id=x))
            
        profesor.nombre = nombre
        profesor.apellido1 = apellido1
        profesor.apellido2= apellido2
        profesor.rut = rut
        profesor.fecha_nacimiento = fecha_nacimiento
        profesor.email = email
        profesor.telefono = telefono
        profesor.genero =genero
        profesor.especialidad = especialidad
        profesor.save()
        
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
    
def edicion_alumno(request, alum_id):
    alumno = Alumno.objects.filter(alum_id=alum_id).first()    
    cursos = Curso.objects.all()    
    colegios = Colegio.objects.all()    
    
    return render (request, 'gestionAcademica/configuracion_usuarios/edicion_alumno.html',
                   {
                       "alumno":alumno,
                       "cursos":cursos,
                       "colegios":colegios
                   })

def editar_alumno(request):
    id=request.POST.get('id')
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
    
    alumno = Alumno.objects.get(pk=id)
    curso = Curso.objects.get(pk=id_curso)
    colegio = Colegio.objects.get(pk=id_colegio)
    
    alumno.nombre = nombre
    alumno.apellido1 = apellido1
    alumno.apellido2 = apellido2
    alumno.rut = rut
    alumno.fecha_nacimiento=fecha_nacimiento
    alumno.email = email
    alumno.telefono = telefono
    alumno.genero = genero
    alumno.status =status
    alumno.curso = curso
    alumno.colegio = colegio
    alumno.save()
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

def edicion_apoderado(request, apo_id):
    apoderado = Apoderado.objects.filter(apo_id=apo_id).first()
    alumnos = Alumno.objects.all()
    
    return render(request, 'gestionAcademica/configuracion_usuarios/edicion_apoderado.html',
                  {
                      "apoderado":apoderado,
                      "alumnos": alumnos
                  })

def editar_apoderado(request):
        id = int(request.POST.get('id'))
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
        apoderado = Apoderado.objects.get(pk=id)
        
        for x in alumno_nombres:
            alumno_ids.append(int(request.POST.get(x)))
        for x in alumno_ids:
            apoderado.alumno.add(Alumno.objects.get(alum_id=x))
        

        apoderado.nombre= nombre
        apoderado.apellido1= apellido1
        apoderado.apellido2 = apellido2
        apoderado.rut = rut
        apoderado.fecha_nacimiento = fecha_nacimiento
        apoderado.email = email
        apoderado.telefono = telefono
        apoderado.genero = genero
        apoderado.save()
        return redirect('administracion_apoderado')
        
def eliminar_apoderado(self, apo_id):
    
    apoderado= Apoderado.objects.filter(apo_id=apo_id).delete()
    
    if len(apoderado)>0:
        datos={'message':"Success"}
    else:
        datos={"message":"Alumno not found"}
    
    return redirect('administracion_apoderado')

#-----------------CONFIGURACIÓN DE USUARIOS /------------------------------------


#-----------------CONFIGURACIÓN DE COLEGIO------------------------------------
@login_required
def configuracion_colegio(request):
    
    return render(request, 'gestionAcademica/configuracion_colegio/colegio.html', 
                  {"colegios":Colegio.objects.all()})

def registra_colegio(request):
    
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
    
        return redirect ('configuracion_colegio')

def ingreso_calificacion(request):
    promedio = 0
    notas = Nota.objects.all()
    for nota in notas:
        promedio+=nota.nota_obtenida1
    
    if len(notas) == 0:
        promedio = '0'
    else:
        promedio = promedio/len(notas)
    
    return render(request, 'gestionAcademica/configuracion_academica/ingresaCalificacion.html',
                    {   "promedio":promedio,
                        "notas": Nota.objects.all(),
                        "alumnos": Alumno.objects.all(),
                        "profesores": Profesor.objects.all(), 
                        "evaluaciones": Evaluacion.objects.all()
                    })
    
def registra_nota(request):
    if request.method == "POST":
        id_alumno = request.POST.get('alumno')
        id_evaluacion = request.POST.get('evaluacion')
        id_profesor = request.POST.get("profesor")
        

        
        
        nota_obtenida1 = request.POST.get('nota_obtenida1')
        
        if nota_obtenida1 == '':
            nota_obtenida1 = 0.00
            print('Aqui ->',nota_obtenida1)
            
        nota_obtenida1_float = float(nota_obtenida1)
        alumno = Alumno.objects.get(pk=id_alumno)
        evaluacion = Evaluacion.objects.get(pk=id_evaluacion)
        profesor = Profesor.objects.get(pk=id_profesor)
        nota = Nota.objects.create(
            nota_obtenida1 = nota_obtenida1_float,
            alumno = alumno,
            evaluacion = evaluacion, 
            profesor = profesor 
        )
        return redirect('ingreso_calificacion')

def edicion_nota(request,nota_id): 
    nota = Nota.objects.filter(nota_id=nota_id).first()
    alumnos = Alumno.objects.all()
    profesores = Profesor.objects.all()
    evaluaciones = Evaluacion.objects.all()
    return render (request, 'gestionAcademica/configuracion_academica/editar_nota.html', {
        "nota": nota,
        "alumnos":alumnos,
        "profesores":profesores,
        "evaluaciones":evaluaciones
    }) 

def editar_nota(request):
    if request.method== "POST":
        id = int(request.POST.get('id'))
        id_alumno = request.POST.get('alumno')
        id_profesor =request.POST.get('profesor')
        id_evaluacion = request.POST.get('evaluacion')
        nota_obtenida1 = request.POST.get('nota_obtenida1')
        
        if nota_obtenida1 == '':
            nota_obtenida1 = 0.00
            print('Aqui ->',nota_obtenida1)

        nota_obtenida1_float = float(nota_obtenida1)
        
        nota = Nota.objects.get(pk=id)
        alumno = Alumno.objects.get(pk=id_alumno)
        profesor = Profesor.objects.get(pk=id_profesor)
        evaluacion = Evaluacion.objects.get(pk=id_evaluacion)
        
        nota.alumno = alumno
        nota.profesor = profesor
        nota.evaluacion = evaluacion
        nota.nota_obtenida1 = nota_obtenida1_float 
        nota.save()
        
        return redirect('ingreso_calificacion')
    
def eliminar_nota(self, nota_id):
    nota= Nota.objects.filter(nota_id=nota_id).delete()
    
    if len(nota)>0:
        datos={'message':"Success"}
    else:
        datos={"message":"Alumno not found"}
    
    return redirect('ingreso_calificacion')

def configuracion_evaluacion(request):
    evaluaciones = Evaluacion.objects.all()
    asignaturas = Asignatura.objects.all()
    
    return render(request, 'gestionAcademica/configuracion_academica/evaluacion.html',
                    {
                        "evaluaciones": evaluaciones,
                        "asignaturas": asignaturas
                    })
    
def registra_evaluacion(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        fecha = request.POST.get('fecha')
        id_asignatura = request.POST.get('asignatura')
        
        asignatura = Asignatura.objects.get(pk=id_asignatura)
        
        evaluacion = Evaluacion.objects.create(
            nombre = nombre,
            fecha = fecha,
            asignatura = asignatura
        )
        
        return redirect('configuracion_evaluacion')

def edicion_evaluacion(request, eva_id):
    evaluacion = Evaluacion.objects.filter(eva_id=eva_id).first()
    asignaturas = Asignatura.objects.all()
    
    return render (request, 'gestionAcademica/configuracion_academica/editar_evaluacion.html', {
        "evaluacion": evaluacion,
        "asignaturas":asignaturas,
    }) 
    
def editar_evaluacion(request):
    if request.method == "POST":
        id= int(request.POST.get('id'))
        id_asignatura = request.POST.get('asignatura')
        nombre = request.POST.get('nombre')
        fecha= request.POST.get('fecha')
        
        asignatura = Asignatura.objects.get(pk=id_asignatura)
        evaluacion = Evaluacion.objects.get(eva_id=id)
        
        evaluacion.nombre = nombre
        evaluacion.fecha = fecha
        evaluacion.asignatura = asignatura
        evaluacion.save()
        
        return redirect("configuracion_evaluacion")
    
def eliminar_evaluacion(request, eva_id):
    evaluacion= Evaluacion.objects.filter(eva_id=eva_id).delete()
    
    if len(evaluacion)>0:
        datos={'message':"Success"}
    else:
        datos={"message":"Alumno not found"}
    
    return redirect('configuracion_evaluacion')
#-----------------CONFIGURACIÓN DE COLEGIO------------------------------------

