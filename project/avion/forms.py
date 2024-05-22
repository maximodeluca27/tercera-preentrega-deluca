from django import forms

from . import models 

class AvionForm(forms.ModelForm):
    class Meta: 
        model=models.Avion
        fields={"fabricante","modelo","avion_origen_id","fecha_incorporacion","capacidad_maxima"}

class AeropuertoForm(forms.ModelForm):
    class Meta: 
        model=models.Aeropuerto
        fields={"nombre","pais_origen"}