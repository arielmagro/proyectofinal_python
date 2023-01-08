from django import forms
from ejemplo.models import Familiar, Seguro, DatosPersonales

class Buscar(forms.Form):
  nombre = forms.CharField(max_length=100)

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte']

class DatospersonalesForm(forms.ModelForm):
  class Meta:
    model = DatosPersonales
    fields = ['nombre', 'direccion', 'numero_pasaporte', 'numero_dni', 'factorSanguineo']

class SeguroForm(forms.ModelForm):
  class Meta:
    model = Seguro
    fields = ['nombre', 'tipoDePlan', 'numeroSocio']
