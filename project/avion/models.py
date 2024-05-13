from django.db import models

class Cliente(models.Model):
    nombre=models.CharField(max_length=40)
    pasajes=models.IntegerField()

    def __str__(self) -> str:
        return self.nombre

class Avion(models.Model):
    fabricante=models.CharField(max_length=40)
    modelo=models.CharField(max_length=40)

    def __str__(self) -> str:
        return f"{self.fabricante} {self.modelo} "
# Create your models here.
