from django.db import models

class Post(models.Model):
    titulo=models.CharField(max_length=100)
    sub_titulo=models.CharField(max_length=100)
    texto=models.TextField(max_length=300)
    publicado_el=models.DateTimeField()
