"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from ejemplo.views import (index, index_dos, index_tres,
                           imc, monstrar_familiares, BuscarFamiliar, AltaFamiliar,
                           ActualizarFamiliar, ActualizarDatos_Personales , Actualizarseguro,
                           AltaDatos_Personales , AltaSeguro, monstrar_Datos_Personales , monstrar_seguro ,
                           BuscarDatosPersonales , BuscarSeguro, FamiliarList, FamiliarCrear, FamiliarBorrar, FamiliarActualizar)
#from blog.views import index as blog_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index),
    path('saludar/<nombre>/<apellido>/', index_dos),
    path('mostrar-notas/', index_tres),
    path('imc/<int:peso>/<int:altura>', imc),
    path('mi-familia/', monstrar_familiares),
#    path('blog/', blog_index),
    path('mi-familia/buscar', BuscarFamiliar.as_view()),  # NUEVA RUTA PARA BUSCAR FAMILIAR
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    path('seguro/actualizar/<int:pk>', Actualizarseguro.as_view()),
    path('datosPersonales/actualizar/<int:pk>', ActualizarDatos_Personales.as_view()),
    path('seguro/alta', AltaSeguro.as_view()),
    path('mis-datos-personales/alta', AltaDatos_Personales.as_view()),
    path('seguro/', monstrar_seguro),
    path('datosPersonales/', monstrar_Datos_Personales),
    path('seguro/buscar', BuscarSeguro.as_view()),
    path('datosPersonales/buscar', BuscarDatosPersonales.as_view()),
    path('panel-familia/', FamiliarList.as_view()),
    path('panel-familia/crear', FamiliarCrear.as_view()),
    path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view()),
    path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view()),
]