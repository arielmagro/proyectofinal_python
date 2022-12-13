from django import forms
from ejemplo.models import Familiar, Seguro , Datos_Personales

class Buscar(forms.Form):
  nombre = forms.CharField(max_length=100)

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte']


class Datos_PersonalesForm(forms.ModelForm):
  class Meta:
    model = Datos_Personales
    fields = ['nombre', 'direccion', 'numero_pasaporte','numero_dni', 'FactorSanguineo']

class SeguroForm(forms.ModelForm):
  class Meta:
    model = Seguro
    fields = ['nombre', 'tipodeplan', 'numero_socio']