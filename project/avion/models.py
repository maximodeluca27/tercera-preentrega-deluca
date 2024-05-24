from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Usuario(models.Model):
    nombre=models.CharField(max_length=40,default="nombre por defecto")
    usuario=models.OneToOneField(User,on_delete=models.CASCADE,related_name="usuario",null=True,blank=True)
    celular=models.IntegerField()
    avatar=models.ImageField(upload_to="avatares",null=True,blank=True)

    def __str__(self) -> str:
        return self.usuario.username
    
class Aeropuerto(models.Model):
    nombre=models.CharField(max_length=40)
    pais_origen=models.CharField(max_length=40)
    def __str__(self) -> str:
        return f"{self.nombre} {self.pais_origen} "

class Avion(models.Model):
    fabricante=models.CharField(max_length=40)
    modelo=models.CharField(max_length=40)
    avion_origen_id=models.ForeignKey(Aeropuerto,on_delete=models.SET_NULL,null=True)
    fecha_incorporacion=models.DateField(default=timezone.now)
    capacidad_maxima=models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.fabricante} {self.modelo} "
    

# Create your models here.
