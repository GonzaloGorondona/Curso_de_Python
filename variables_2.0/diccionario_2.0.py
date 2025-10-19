#diccionario con dict

diccionario = dict(nombre="Gonzalo", apellido ="Gorondona")

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {("Gonzalo","rancio","jaja")}

#creando diccionarios con fromkeys()
diccionario = dict.fromkeys(["nombre","apellido"]) 

#creando diccionarios con fromkeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre","apellido"],"no se")

print(diccionario)