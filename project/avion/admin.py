from django.contrib import admin
from .models import Cliente,Avion,Aeropuerto

admin.site.register(Cliente)
admin.site.register(Aeropuerto)
admin.site.register(Avion)

# Register your models here.
