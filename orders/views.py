from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"login.html")

# Create your views here.
def login(request):
    return HttpResponse("Project 3: TODO")

def registro(request):
    return render(request,"registrarse.html")

def menu(request):
    return render(request,"menu.html")
def detalles_pizza(request):
    return render(request,"detalles_pizza.html")
