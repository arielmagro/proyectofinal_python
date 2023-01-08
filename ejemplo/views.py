from django.shortcuts import render, get_object_or_404
from ejemplo.models import Familiar, Seguro, DatosPersonales
from ejemplo.forms import Buscar, FamiliarForm, SeguroForm, DatospersonalesForm # <--- NUEVO IMPORT
from django.views import View # <-- NUEVO IMPORT
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

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

def monstrar_datosPersonales(request):
  lista_datosPersonales = DatosPersonales.objects.all()
  return render(request, "ejemplo/datosPersonales.html", {"lista_datosPersonales": lista_datosPersonales})

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

class BuscarSeguro(View):
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
            lista_seguro = Seguro.objects.filter(nombre__icontains=nombre).all()
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form,
                                                        'lista_seguro':lista_seguro})
        return render(request, self.template_name, {"form": form})

class BuscarDatosPersonales(View):
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
            lista_datosPersonales= DatosPersonales.objects.filter(nombre__icontains=nombre).all()
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form,
                                                        'lista_datosPersonales':lista_datosPersonales})
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
class AltaDatosPersonales(View):

    form_class = DatospersonalesForm
    template_name = 'ejemplo/alta_datosPersonales.html'
    initial = {"nombre": "", "direccion": "", "numero_pasaporte": "", "numero_dni": "", "factorSanguineo": ""}

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
    initial = {"nombre": "", "tipoDePlan": "", "numeroSocio": ""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito pa persona con numero de socio {form.cleaned_data.get('numeroSocio')}"
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
class ActualizarDatosPersonales(View):
    form_class = DatospersonalesForm
    template_name = 'ejemplo/actualizar_datosPersonales.html'
    initial = {"nombre": "", "direccion": "", "numero_pasaporte": "", "numero_dni": "", "factorSanguineo": ""}

    # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
    def get(self, request, pk):
        datosPersonales = get_object_or_404(DatosPersonales, pk=pk)
        form = self.form_class(instance=datosPersonales)
        return render(request, self.template_name, {'form': form, 'datosPersonales': datosPersonales})

    # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
    def post(self, request, pk):
        datosPersonales = get_object_or_404(DatosPersonales, pk=pk)
        form = self.form_class(request.POST, instance=datosPersonales)
        if form.is_valid():
            form.save()
            msg_exito = f"se actualizó con éxito los datos personales de {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form,
                                                        'datosPersonales': datosPersonales,
                                                        'msg_exito': msg_exito})

        return render(request, self.template_name, {"form": form})
class ActualizarSeguro(View):
    form_class = SeguroForm
    template_name = 'ejemplo/actualizar_seguro.html'
    initial = {"nombre": "", "tipoDePlan": "", "numeroSocio": ""}

    # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
    def get(self, request, pk):
        seguro = get_object_or_404(Seguro, pk=pk)
        form = self.form_class(instance=seguro)
        return render(request, self.template_name, {'form': form, 'seguro': seguro})

    # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
    def post(self, request, pk):
        seguro = get_object_or_404(Seguro, pk=pk)
        form = self.form_class(request.POST, instance= seguro)
        if form.is_valid():
            form.save()
            msg_exito = f"se actualizó con éxito el seguro numero {form.cleaned_data.get('numeroSocio')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form,
                                                        'seguro': seguro,
                                                        'msg_exito': msg_exito})

        return render(request, self.template_name, {"form": form})

class FamiliarList(ListView):
  model = Familiar

class FamiliarCrear(CreateView):
  model = Familiar
  success_url = "/panel-familia"
  fields = ["nombre", "direccion", "numero_pasaporte"]

class FamiliarBorrar(DeleteView):
  model = Familiar
  success_url = "/panel-familia"
class FamiliarActualizar(UpdateView):
  model = Familiar
  success_url = "/panel-familia"
  fields = ["nombre", "direccion", "numero_pasaporte"]




