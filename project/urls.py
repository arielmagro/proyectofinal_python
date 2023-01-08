"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from ejemplo.views import (index, index_dos, index_tres,imc,
                           monstrar_familiares, BuscarFamiliar,
                           AltaFamiliar, ActualizarFamiliar,
                           ActualizarSeguro, ActualizarDatosPersonales,
                           AltaSeguro, AltaDatosPersonales, monstrar_seguro,
                           monstrar_datosPersonales, BuscarDatosPersonales, BuscarSeguro,
                           FamiliarList, FamiliarCrear, FamiliarBorrar, FamiliarActualizar)
from blogfinal.views import (index, PostList, Postcrear, DeleteView, PostDetalle,
                             PostActualizar, PostBorrar, UserSingUp, UserLogin,
                             UserLogOut, AvatarActualizar, UserActualizar
                             , MensajeCrear, MensajeListar, MensajeDetalle)

#from blog.views import index as blog_index
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index),
    path('saludar/<nombre>/<apellido>/', index_dos),
    path('mostrar-notas/', index_tres),
    path('imc/<int:peso>/<int:altura>/', imc),
    path('mi-familia/', monstrar_familiares),
    path('mi-familia/buscar/', BuscarFamiliar.as_view()),  # NUEVA RUTA PARA BUSCAR FAMILIAR
    path('mi-familia/alta/', AltaFamiliar.as_view()),  # NUEVA RUTA PARA BUSCAR FAMILIAR
    path('mi-familia/actualizar/<int:pk>/', ActualizarFamiliar.as_view()),
    path('seguro/actualizar/<int:pk>', ActualizarSeguro.as_view()),
    path('datosPersonales/actualizar/<int:pk>/', ActualizarDatosPersonales.as_view()),
    path('mis-datos-personales/alta/', AltaDatosPersonales.as_view()),
    path('mi-seguro/alta/', AltaSeguro.as_view()),
    path('seguro/', monstrar_seguro),
    path('datosPersonales/', monstrar_datosPersonales),
    path('seguro/buscar', BuscarSeguro.as_view()),
    path('datosPersonales/buscar', BuscarDatosPersonales.as_view()),
    path('panel-familia/', FamiliarList.as_view()),
    path('panel-familia/crear/', FamiliarCrear.as_view()),
    path('panel-familia/<int:pk>/borrar/', FamiliarBorrar.as_view()),
    path('panel-familia/<int:pk>/actualizar/', FamiliarActualizar.as_view()),
    path('accounts/profile/', PostList.as_view(), name='profile'),
    path('blogfinal/', index, name='index'),
    path('blogfinal/listar/', PostList.as_view(), name='listar'),
    path('blogfinal/crear/', Postcrear.as_view(), name='crear'),
    path('blogfinal/<int:pk>/borrar/', PostBorrar.as_view(), name='borrar'),
    path('blogfinal/<int:pk>/detalle/', PostDetalle.as_view(), name='detalle'),
    path('blogfinal/<int:pk>/actualizar/', PostActualizar.as_view(), name='actualizar'),
    path('blogfinal/signup/', UserSingUp.as_view(), name='signup'),
    path('blogfinal/login/', UserLogin.as_view(), name='login'),
    path('blogfinal/logout/', UserLogOut.as_view(), name='logout'),
    path('blogfinal/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name='avatar'),
    path('blogfinal/users/<int:pk>/actualizar/', UserActualizar.as_view(), name='user'),
    path('blogfinal/mensajes/crear/', MensajeCrear.as_view(), name="mensajes-crear"),
    path('blogfinal/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="mensajes-detalle"),
    path('blogfinal/mensajes/listar/', MensajeListar.as_view(), name="mensajes-listar"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)