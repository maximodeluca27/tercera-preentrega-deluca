from django.shortcuts import render, redirect
from avion.models import Avion
from avion.forms import AvionForm

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

# Create your views here.
