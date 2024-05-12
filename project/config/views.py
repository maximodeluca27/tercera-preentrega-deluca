from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):
    return HttpResponse("Hola Maxi")

def probandotemplate(request):
  datos={"saludo":"Bienvenido a VirtualPlanes","autor":"Maximo De Luca"}
  return render(request,"template.html",context=datos)