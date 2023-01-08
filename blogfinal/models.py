from django.db import models
from django.contrib.auth.admin import User
class Post(models.Model):
    objects = None
    titulo = models.CharField(max_length=100)
    sub_titulo = models.CharField(max_length=100)
    texto = models.TextField(max_length=3000)
    publicado_el = models.DateTimeField()
    imagen = models.ImageField(upload_to='posteos', null='True', blank=True)
# Create your models here.
class Avatar(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='avatar')
    imagen = models.ImageField(upload_to='avatares', null='True', blank=True)

class Mensaje(models.Model):
    email = models.EmailField()
    nombre = models.CharField(max_length=100)
    texto = models.TextField(max_length=3000)
    enviado_el = models.DateField(auto_now_add=True)