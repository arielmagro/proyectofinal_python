from ejemplo.models import Familiar, Datos_Personales, Seguro
Familiar(nombre="Rosario", direccion="Rio Parana 745", numero_pasaporte=123123).save()
Familiar(nombre="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890).save()
Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345).save()
Familiar(nombre="Florencia", direccion="Rio Parana 745", numero_pasaporte=567567).save()
Familiar(nombre="Caro", direccion="Defensa 20", numero_pasaporte=144444).save()
Datos_Personales(nombre="Caro", direccion="Defensa 20", numero_pasaporte=144444, numero_dni=144444,FactorSanguineo="144444" ).save()
Seguro(nombredeplan="Caro", tipodeplan="Defensa 20", numero_socio=144444).save()

print("Se cargo con éxito los usuarios de pruebas")