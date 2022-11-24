"""NonsLy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *
from gestionAcademica import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('login/',login, name='login'),
    #path('buscar/', views.buscar),
    path('whoweare/', whoweare, name='whoweare'),
    path('soporte/', soporte, name='soporte'),
    path('faq/', faq, name='faq'),
    path('demo/', demo, name='demo'),
    path('configuracion_periodo/', configuracion_periodo, name='configuracion_periodo'),
    path('configuracion_nivel/', configuracion_nivel, name='configuracion_nivel'),
    path('configuracion_curso/', configuracion_curso, name='configuracion_curso'),
    path('configuracion_asignatura/', configuracion_asignatura, name='configuracion_asignatura'),
#-----------------CONFIGURACIÓN DE USUARIOS------------------------------------
    path('administracion/', administracion, name='administracion'),
    path('administracion_profesor/', administracion_profesor, name='administracion_profesor'),
    path('administracion_alumno/', administracion_alumno, name='administracion_alumno'),
    path('administracion_apoderado/', administracion_apoderado, name='administracion_apoderado'),
#-----------------CONFIGURACIÓN DE USUARIOS /------------------------------------
    path('configuracion_colegio/', configuracion_colegio, name='configuracion_colegio'),

]
