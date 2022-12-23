from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView, DetailView
from blogfinal.models import Post

def index(request):
    return render(request,"blogfinal/index.html",{})

class PostList(ListView):
    model = Post

class PostCrear(CreateView):
    model = Post
    success_url = "/blogfinal/listar"
    fields = '__all__'
class PostBorrar(DeleteView):
    model = Post
    success_url = reverse_lazy("borrar")

class PostActualizar(UpdateView):
    model = Post
    success_url = reverse_lazy("actualizar") #"/blogfinal/listar"
    fields = '__all__'
class PostDetalle(DetailView):
    model = Post
    success_url = reverse_lazy("detalle")