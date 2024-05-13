from django.shortcuts import render
from avion.models import Avion

def index(request):
    return render(request,"avion/index.html")

def avion_list(request):
    consulta=Avion.objects.all()
    contexto={"aviones":consulta}
    return render(request,"avion/avion_list.html",contexto)

# Create your views here.
