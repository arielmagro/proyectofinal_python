from ejemplo.models import Familiar, DatosPersonales, Seguro

Familiar(nombre="Rosario", direccion="Rio Parana 745", numero_pasaporte=123123).save()
Familiar(nombre="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890).save()
Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345).save()
Familiar(nombre="Florencia", direccion="Rio Parana 745", numero_pasaporte=567567).save()
Familiar(nombre="Caro", direccion="Rio Parana 745", numero_pasaporte=123123).save()
Familiar(nombre="Ariel", direccion="Rio Parana 745", numero_pasaporte=890890).save()
Familiar(nombre="Sami", direccion="Rio Parana 745", numero_pasaporte=345345).save()
Familiar(nombre="Bebe", direccion="Rio Parana 745", numero_pasaporte=567567).save()
DatosPersonales(nombre="grecia", direccion="Rio Parana 745", numero_pasaporte=345345, numero_dni=345345, factorSanguineo="Rio Parana 745").save()
DatosPersonales(nombre="holanda", direccion="Rio Parana 745", numero_pasaporte=345345, numero_dni=345345, factorSanguineo="Rio Parana 745").save()
DatosPersonales(nombre="polonia", direccion="Rio Parana 745", numero_pasaporte=345345, numero_dni=345345, factorSanguineo="Rio Parana 745").save()
Seguro(nombre="Bebe", tipoDePlan="Rio Parana 745", numeroSocio=567567).save()
Seguro(nombre="nina", tipoDePlan="Rio Parana 745", numeroSocio=567567).save()
Seguro(nombre="negra", tipoDePlan="Rio Parana 745", numeroSocio=567567).save()
Seguro(nombre="bruna", tipoDePlan="Rio Parana 745", numeroSocio=567567).save()
print("Se cargo con éxito los usuarios de pruebas")