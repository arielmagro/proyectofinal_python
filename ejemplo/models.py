from django.db import models
class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    def __str__(self):
        return f"{self.nombre}, {self.direccion}, {self.numero_pasaporte}, {self.id}"
class DatosPersonales(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    numero_dni = models.IntegerField()
    factorSanguineo= models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nombre}, {self.numero_pasaporte}, {self.numero_dni}, {self.factorSanguineo}, {self.direccion}, {self.id}"
class Seguro(models.Model):
    nombre = models.CharField(max_length=100)
    tipoDePlan = models.CharField(max_length=200)
    numeroSocio = models.IntegerField()
    def __str__(self):
        return f"{self.nombre}, {self.tipoDePlan},{self.numeroSocio}, {self.id}"