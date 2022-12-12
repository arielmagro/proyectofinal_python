
from django.shortcuts import render, get_object_or_404
from ejemplo.models import Familiar, Seguro , Datos_Personales
from ejemplo.forms import Buscar, FamiliarForm,SeguroForm ,Datos_PersonalesForm
from django.views import View

def index(request):
    return render(request, "ejemplo/saludar.html")
def index_dos(request):
    return render(request, "ejemplo/saludar.html")
def index_tres(request):
    return render(request, "ejemplo/saludar.html")
def imc(request):
    return render(request, "ejemplo/saludar.html")
def monstrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})
def monstrar_Datos_Personales(request):
    lista_datos_personales = Datos_Personales.objects.all()
    return render(request, "ejemplo/datosPersonales.html", {"lista_datos_personales": lista_datos_personales})
def monstrar_seguro(request):
    lista_seguro = Seguro.objects.all()
    return render(request, "ejemplo/seguro.html", {"lista_seguro": lista_seguro})

class BuscarFamiliar(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all()
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form,
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})

class BuscarFamiliar(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all()
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form,
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})

class BuscarFamiliar(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all()
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form,
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})

class AltaFamiliar(View):
    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre": "", "direccion": "", "numero_pasaporte": ""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form,
                                                        'msg_exito': msg_exito})

        return render(request, self.template_name, {"form": form})

class AltaDatos_Personales(View):
    form_class = Datos_PersonalesForm
    template_name = 'ejemplo/alta_Datos_Personales.html'
    initial = {"nombre": "", "direccion": "", "numero_pasaporte": "", "numero_dni": "", "FactorSanguineo": "" }

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito los datos personales de {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form,
                                                        'msg_exito': msg_exito})

        return render(request, self.template_name, {"form": form})

class AltaSeguro(View):
    form_class = SeguroForm
    template_name = 'ejemplo/alta_seguro.html'
    initial = {"nombredeplan": "", "tipodeplan": "", "numero_socio": "" }

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el seguro de el {form.cleaned_data.get('numero_socio')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form,
                                                        'msg_exito': msg_exito})

        return render(request, self.template_name, {"form": form})

class ActualizarFamiliar(View):
    form_class = FamiliarForm
    template_name = 'ejemplo/actualizar_familiar.html'
    initial = {"nombre": "", "direccion": "", "numero_pasaporte": ""}

    # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
    def get(self, request, pk):
        familiar = get_object_or_404(Familiar, pk=pk)
        form = self.form_class(instance=familiar)
        return render(request, self.template_name, {'form': form, 'familiar': familiar})

    # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
    def post(self, request, pk):
        familiar = get_object_or_404(Familiar, pk=pk)
        form = self.form_class(request.POST, instance=familiar)
        if form.is_valid():
            form.save()
            msg_exito = f"se actualizó con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form,
                                                        'familiar': familiar,
                                                        'msg_exito': msg_exito})

        return render(request, self.template_name, {"form": form})

class ActualizarDatos_Personales(View):
    form_class = Datos_PersonalesForm
    template_name = 'ejemplo/ActualizarDatos_Personales.html'
    initial = {"nombre": "", "direccion": "", "numero_pasaporte": "", "numero_dni": "", "FactorSanguineo": ""}

    # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
    def get(self, request, pk):
        datospersonales = get_object_or_404(Datos_Personales, pk=pk)
        form = self.form_class(instance=datospersonales)
        return render(request, self.template_name, {'form': form, 'datospersonales': datospersonales})

    # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
    def post(self, request, pk):
        datospersonales = get_object_or_404(Datos_Personales, pk=pk)
        form = self.form_class(request.POST, instance=datospersonales)
        if form.is_valid():
            form.save()
            msg_exito = f"se actualizó con éxito los datos personales de  {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form,
                                                        'familiar': datospersonales,
                                                        'msg_exito': msg_exito})

        return render(request, self.template_name, {"form": form})

class Actualizarseguro(View):
    form_class = SeguroForm
    template_name = 'ejemplo/Actualizar_seguro.html'
    initial = {"nombredeplan": "", "tipodeplan": "", "numero_socio": ""}

    # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
    def get(self, request, pk):
        seguro = get_object_or_404(Seguro, pk=pk)
        form = self.form_class(instance=seguro)
        return render(request, self.template_name, {'form': form, 'seguro': seguro})

    # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
    def post(self, request, pk):
        seguro = get_object_or_404(Seguro, pk=pk)
        form = self.form_class(request.POST, instance=seguro)
        if form.is_valid():
            form.save()
            msg_exito = f"se actualizó con éxito el seguro numero  {form.cleaned_data.get('numero_socio')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form,
                                                        'seguro': seguro,
                                                        'msg_exito': msg_exito})

        return render(request, self.template_name, {"form": form})