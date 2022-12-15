from django.contrib import admin

from gestionAcademica.models import Profesor, Colegio, Alumno, Apoderado, Curso, Asignatura, Clase, Evaluacion, Periodo, Nota, Nivel

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ("prof_id","nombre", "apellido1", "rut", "email")
    search_fields = ("prof_id","nombre", "apellido1", "rut", "email")
    
class ColegioAdmin(admin.ModelAdmin):
    list_display = ("col_id", "rbd","nombre", "sigla")
    search_fields = ("col_id", "rbd","nombre", "sigla")
    
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ("alum_id", "nombre", "apellido1", "rut", "email")
    search_fields = ("alum_id", "nombre", "apellido1", "rut", "email")
    
class ApoderadoAdmin(admin.ModelAdmin):
       list_display = ("apo_id", "nombre", "apellido1", "rut", "email")
       search_fields = ("apo_id", "nombre", "apellido1", "rut", "email")
       
class CursoAdmin(admin.ModelAdmin):
       list_display = ("curso_id", "nombre", "capacidad", "nivel", "annio_academico")
       search_fields = ("curso_id", "nombre", "capacidad")
     
class AsignaturaAdmin(admin.ModelAdmin):
       list_display = ("asig_id", "nombre", "curso")
       search_fields = ("curso_id", "nombre")

class ClaseAdmin(admin.ModelAdmin):
       list_display = ("clase_id", "asig", "prof", "per")
       search_fields = ("clase_id",)
       
class EvaluacionAdmin(admin.ModelAdmin):
       list_display = ("eva_id", "nombre", "fecha", "asignatura")
       search_fields = ("eva_id", "nombre", "fecha")
       
class PeriodoAdmin(admin.ModelAdmin):
       list_display = ("per_id", "fecha_inicio", "fecha_fin")
       search_fields = ("per_id",)

class NotaAdmin(admin.ModelAdmin):
       list_display = ("nota_id", "nota_obtenida1", "alumno", "profesor", "evaluacion")
       search_fields = ("per_id",)
class NivelAdmin(admin.ModelAdmin):
       list_display = ("niv_id", "nombre")
       search_fields = ("niv_id","nombre")
       
       
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Colegio, ColegioAdmin)
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Apoderado, ApoderadoAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Asignatura, AsignaturaAdmin)
admin.site.register(Clase, ClaseAdmin)
admin.site.register(Evaluacion, EvaluacionAdmin)


admin.site.register(Nivel, NivelAdmin)

admin.site.register(Periodo, PeriodoAdmin)
admin.site.register(Nota, NotaAdmin)
