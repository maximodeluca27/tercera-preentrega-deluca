from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from avion.models import Avion
from avion.models import Aeropuerto
from avion.forms import AvionForm
from avion.forms import AeropuertoForm
from django.views.generic import CreateView,ListView, DetailView, UpdateView, DeleteView

def index(request):
    return render(request,"avion/index.html")

class Aeropuertos_list(ListView):
    model=Aeropuerto
    context_object_name="aeropuertos"
    template_name="avion/aeropuertos_list.html"
    def get_queryset(self) -> QuerySet[Any]:
        if self.request.GET.get("busqueda"):
            busqueda=self.request.GET.get("busqueda")
            consulta=Aeropuerto.objects.filter(nombre__icontains=busqueda)
        else:
            consulta=Aeropuerto.objects.all()
        return consulta

# class Aeropuerto_create(CreateView):
   # model=Aeropuerto
   # form_class=AeropuertoForm
   # success_url = reversed("avion:aeropuertos_list")
   # template_name="avion/aeropuerto_create.html"
    
    
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

#def aeropuertos_list(request):
   # busqueda=request.GET.get("busqueda",None)
   # if busqueda:
   #     print(busqueda)
    #    consulta=Aeropuerto.objects.filter(nombre__icontains=busqueda)
   # else:
    #     consulta=Aeropuerto.objects.all()
  #  contexto={"aeropuertos":consulta}
  #  return render(request,"avion/aeropuertos_list.html",contexto)

def aeropuerto_detail(request,pk:int):
    consulta=Aeropuerto.objects.get(id=pk)
    contexto={"aeropuerto":consulta}
    return render(request,"avion/aeropuerto_detail.html",contexto)

def aeropuerto_update(request, pk:int):
    consulta=Aeropuerto.objects.get(id=pk)
    if request.method == "POST":
        form=AeropuertoForm(request.POST,instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("avion:aeropuertos_list")
    else:
        form=AeropuertoForm(instance=consulta)
    return render(request,"avion/aeropuerto_create.html",{"form":form})

def aeropuerto_delete(request, pk:int):
    consulta=Aeropuerto.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("avion:aeropuertos_list")
    return render(request,"avion/aeropuerto_confirm_delete.html",{"object":consulta})

# Create your views here.
