from django.urls import path
#from django.contrib.auth import LogoutView, logout_then_login, LoginView, redirect_to_login
from django.contrib.auth import views as auth_views
from Website import views


urlpatterns = [
    path('', views.index, name='index'),
    #path('login/', views.login, name='login'),
    path('whoweare/', views.whoweare, name='whoweare'),
    path('soporte/', views.soporte, name='soporte'),
    path('faq/', views.faq, name='faq'),
    path('demo/', views.demo, name='demo'),
    path('login/', views.login, name='login'),
    

   
]
