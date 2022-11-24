from django.contrib import admin

from gestionAcademica.models import Profesor, Colegio,Alumno, Apoderado, Curso, Asignatura, Clase, Evaluacion, Periodo

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
       
""" class CursoAdmin(admin.ModelAdmin):
       list_display = ("curso_id", "nombre", "apellido1", "rut", "email")
       search_fields = ("apo_id", "nombre", "apellido1", "rut", "email") """
     

admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Colegio, ColegioAdmin)
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Apoderado, ApoderadoAdmin)
""" admin.site.register(Apoderado, ApoderadoAdmin)
admin.site.register(Apoderado, ApoderadoAdmin)
admin.site.register(Apoderado, ApoderadoAdmin)
admin.site.register(Apoderado, ApoderadoAdmin)
admin.site.register(Apoderado, ApoderadoAdmin) """
