from django.urls import path
from gestionAcademica import views


urlpatterns = [

    path('configuracion_periodo/', views.configuracion_periodo, name='configuracion_periodo'),
    
    path('configuracion_nivel/', views.configuracion_nivel, name='configuracion_nivel'),
    path('registra_nivel/', views.registra_nivel, name='registra_nivel'),
    path('eliminar_nivel/<niv_id>', views.eliminar_nivel, name='eliminar_nivel'),
    
    path('configuracion_curso/', views.configuracion_curso, name='configuracion_curso'),
    path('registra_curso/', views.registra_curso, name='registra_curso'),
    path('eliminar_curso/<curso_id>', views.eliminar_curso, name='eliminar_curso'),
    
    path('configuracion_asignatura/', views.configuracion_asignatura, name='configuracion_asignatura'),
    path('registra_asignatura/', views.registra_asignatura, name='registra_asignatura'),
    path('eliminar_asignatura/<asig_id>', views.eliminar_asignatura, name='eliminar_asignatura'),
    
#-----------------CONFIGURACIÓN DE USUARIOS------------------------------------
    path('', views.administracion, name='administracion'),
    path('administracion_profesor/', views.administracion_profesor, name='administracion_profesor'),
    path('registra_profesor/', views.registra_profesor, name='registra_profesor'),
    path('eliminar_profesor/<prof_id>', views.eliminar_profesor, name='eliminar_profesor'),
    
    path('administracion_alumno/', views.administracion_alumno, name='administracion_alumno'),
    path('registra_alumno/', views.registra_alumno, name='registra_alumno'),
    path('eliminar_alumno/<alum_id>', views.eliminar_alumno, name='eliminar_alumno'),
    
    path('administracion_apoderado/', views.administracion_apoderado, name='administracion_apoderado'),
    path('registra_apoderado/', views.registra_apoderado, name='registra_apoderado'),
    path('eliminar_apoderado/<apo_id>', views.eliminar_apoderado, name='eliminar_apoderado'),
    
#-----------------CONFIGURACIÓN DE USUARIOS /------------------------------------
    path('configuracion_colegio/', views.configuracion_colegio, name='configuracion_colegio'),

]