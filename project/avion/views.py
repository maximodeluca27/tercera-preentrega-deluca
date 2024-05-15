from django.shortcuts import render, redirect
from avion.models import Avion
from avion.models import Aeropuerto
from avion.forms import AvionForm
from avion.forms import AeropuertoForm

def index(request):
    return render(request,"avion/index.html")

def avion_list(request):
    consulta=Avion.objects.all()
    contexto={"aviones":consulta}
    return render(request,"avion/avion_list.html",contexto)

def avion_create(request):
    if request.method == "POST":
        form=AvionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("avion:avion_list")
    else:
        form=AvionForm()
    return render(request,"avion/avion_create.html",{"form":form})

def aeropuerto_create(request):
    if request.method == "POST":
        form=AeropuertoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("avion:aeropuertos_list")
    else:
        form=AeropuertoForm()
    return render(request,"avion/aeropuerto_create.html",{"form":form})

def aeropuertos_list(request):
    consulta=Aeropuerto.objects.all()
    contexto={"aeropuertos":consulta}
    return render(request,"avion/aeropuertos_list.html",contexto)

# Create your views here.
