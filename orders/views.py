from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request,"login.html")

# Create your views here.
def login(request):
    return HttpResponse("Project 3: TODO")

def registro(request):
    if request.method == "POST":
        username = request.POST["usuario"]
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        password = request.POST["password"]   
        email = request.POST["email"]

        User.objects.create_user(username,nombre,apellido,password,email)

        return HttpResponse("ingresado")

        #return render(request)

    return render(request,"orders/registrarse.html")

def menu(request):
    return render(request,"menu.html")
def detalles_pizza(request):
    return render(request,"detalles_pizza.html")
