from django.shortcuts import render

# Create your views here.
def index(request):
    
    return render(request,'Website/index.html')

def login(request):

    return render(request,'Website/login/login.html')

def soporte(request):
    
    return render(request,'Website/soporte/soporte.html')

def faq(request):
    
    return render(request,'Website/faq/faq.html')

def whoweare(request):
    
    return render(request,'Website/whoweare/devs.html')

def demo(request):
    
    return render(request,'Website/demo/demo.html')

#-----------------WEBSITE /------------------------------------
