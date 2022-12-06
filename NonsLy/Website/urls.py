from django.urls import path
from Website import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('whoweare/', views.whoweare, name='whoweare'),
    path('soporte/', views.soporte, name='soporte'),
    path('faq/', views.faq, name='faq'),
    path('demo/', views.demo, name='demo'),
    
]
