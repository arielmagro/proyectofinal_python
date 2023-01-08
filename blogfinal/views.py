from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from blogfinal.models import Post
from blogfinal.forms import UsuarioForm
from django.contrib.auth.mixins import LoginRequiredMixin
from blogfinal.models import Avatar, Mensaje
from django.contrib.auth.admin import User

@login_required
def index(request):
    posts = Post.objects.order_by('-publicado_el').all()
    return render(request, "blogfinal/index.html", {"posts": posts})

class PostList(ListView):
    model = Post

class Postcrear(LoginRequiredMixin , CreateView):
    model = Post
    success_url =reverse_lazy("listar") #"/blogfinal/listar"
    fields = '__all__'

class PostBorrar(LoginRequiredMixin , DeleteView):
    model = Post
    success_url = reverse_lazy('listar')

class PostActualizar(LoginRequiredMixin , UpdateView):
    model = Post
    success_url = reverse_lazy("listar") #"/blogfinal/listar"
    fields = '__all__'
class PostDetalle(DetailView):
    model = Post
    success_url = reverse_lazy("detalle")

class UserSingUp(CreateView):
    form_class = UsuarioForm
    template_name = 'registration/signup.html'
    success_url= reverse_lazy('listar')

class UserLogin(LoginView):
    next_page = reverse_lazy('listar')

class UserLogOut(LogoutView):
    next_page = reverse_lazy('listar')

class AvatarActualizar(UpdateView):
    model = Avatar
    fields = ['imagen']
    success_url = reverse_lazy('listar')

class UserActualizar(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('listar')
class MensajeDetalle(LoginRequiredMixin, DetailView):
    model = Mensaje

class MensajeListar(LoginRequiredMixin, ListView):
    model = Mensaje

class MensajeCrear(CreateView):
    model = Mensaje
    success_url = reverse_lazy("mensajes-crear")
    fields = ['nombre', 'email', 'texto']

class MensajeBorrar(LoginRequiredMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy("mensajes-listar")
