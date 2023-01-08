from django.urls import path, include
from gestionAcademica import views
from Website import views as v_web
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
urlpatterns = [

    path('configuracion_periodo/', views.configuracion_periodo, name='configuracion_periodo'),
    
    path('configuracion_nivel/', views.configuracion_nivel, name='configuracion_nivel'),
    path('registra_nivel/', views.registra_nivel, name='registra_nivel'),
    path('eliminar_nivel/<niv_id>', views.eliminar_nivel, name='eliminar_nivel'),
    path('edicion_nivel/<niv_id>', views.edicion_nivel, name='edicion_nivel'),
    path('editar_nivel/', views.editar_nivel, name='editar_nivel'),
    
    path('configuracion_curso/', views.configuracion_curso, name='configuracion_curso'),
    path('registra_curso/', views.registra_curso, name='registra_curso'),
    path('eliminar_curso/<curso_id>', views.eliminar_curso, name='eliminar_curso'),
    path('edicion_curso/<curso_id>', views.edicion_curso, name='edicion_curso'),
    path('editar_curso/', views.editar_curso, name='editar_curso'),
    
    path('configuracion_asignatura/', views.configuracion_asignatura, name='configuracion_asignatura'),
    path('registra_asignatura/', views.registra_asignatura, name='registra_asignatura'),
    path('eliminar_asignatura/<asig_id>', views.eliminar_asignatura, name='eliminar_asignatura'),
    path('edicion_asignatura/<asig_id>', views.edicion_asignatura, name='edicion_asignatura'),
    path('editar_asignatura/', views.editar_asignatura, name='editar_asignatura'),
    
#-----------------CONFIGURACIÓN DE USUARIOS------------------------------------
    path('', views.administracion, name='administracion'),
    path('administracion_profesor/', views.administracion_profesor, name='administracion_profesor'),
    path('registra_profesor/', views.registra_profesor, name='registra_profesor'),
    path('eliminar_profesor/<prof_id>', views.eliminar_profesor, name='eliminar_profesor'),
    path('edicion_profesor/<prof_id>', views.edicion_profesor, name='edicion_profesor'),
    path('editar_profesor/', views.editar_profesor, name='editar_profesor'),
    
    
    path('administracion_alumno/', views.administracion_alumno, name='administracion_alumno'),
    path('registra_alumno/', views.registra_alumno, name='registra_alumno'),
    path('eliminar_alumno/<alum_id>', views.eliminar_alumno, name='eliminar_alumno'),
    path('edicion_alumno/<alum_id>', views.edicion_alumno, name='edicion_alumno'),
    path('editar_alumno/', views.editar_alumno, name='editar_alumno'),
    
    path('administracion_apoderado/', views.administracion_apoderado, name='administracion_apoderado'),
    path('registra_apoderado/', views.registra_apoderado, name='registra_apoderado'),
    path('eliminar_apoderado/<apo_id>', views.eliminar_apoderado, name='eliminar_apoderado'),
    path('edicion_apoderado/<apo_id>', views.edicion_apoderado, name='edicion_apoderado'),
    path('editar_apoderado/', views.editar_apoderado, name='editar_apoderado'),
#--------------------------------- CONFIGURACIÓN DE USUARIOS /------------------------------------

#---------------------------------CONFIGURACIÓN NOTAS ---------------------------
    path('ingreso_calificacion/', views.ingreso_calificacion,name ='ingreso_calificacion'),
    path('registra_nota/', views.registra_nota,name ='registra_nota'),
    path('eliminar_nota/<nota_id>', views.eliminar_nota,name ='eliminar_nota'),
    path('edicion_nota/<nota_id>', views.edicion_nota,name ='edicion_nota'),
    path('editar_nota/', views.editar_nota,name ='editar_nota'),

    path('configuracion_evaluacion/', views.configuracion_evaluacion ,name ='configuracion_evaluacion'),
    path('registra_evaluacion/', views.registra_evaluacion, name ='registra_evaluacion'),
    path('eliminar_evaluacion/<eva_id>', views.eliminar_evaluacion, name ='eliminar_evaluacion'),
    path('edicion_evaluacion/<eva_id>', views.edicion_evaluacion,name ='edicion_evaluacion'),
    path('editar_evaluacion/', views.editar_evaluacion,name ='editar_evaluacion'),
    
    path('configuracion_colegio/', views.configuracion_colegio, name='configuracion_colegio'),
    path('registra_colegio/', views.registra_colegio, name='registra_colegio'),
    #path('accounts/logout/', auth_views.LogoutView.as_view(template_name='Website/login/login.html'),  name='logout'),
    #path('', include('Website.urls')),
]
