from django.db import models

# Create your models here.
from django.db import models
class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    def __str__(self):
        return f"{self.nombre}, {self.numero_pasaporte}, {self.id}"

class Datos_Personales(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    numero_dni = models.IntegerField()
    FactorSanguineo = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nombre},{self.direccion},{self.numero_pasaporte},{self.numero_dni},{self.FactorSanguineo} {self.id}"

class Seguro(models.Model):
    nombredeplan = models.CharField(max_length=100)
    tipodeplan = models.CharField(max_length=200)
    numero_socio = models.IntegerField()
    def __str__(self):
        return f"{self.nombredeplan}, {self.numero_socio},{self.tipodeplan} {self.id}"