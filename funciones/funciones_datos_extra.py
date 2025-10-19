#creando una funcion con tres parametros
def frase (nombre,apellido,adjetivo):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

frase_resultante = frase("Gonzalo","Gorondona", "vicio")
print(frase_resultante)

#utilizando keyboards arguments
frase_resultante = frase(adjetivo = "capo", nombre = "Gonzalo", apellido= "Gorondona")

#creando la misma funcion con un parametro opcional y un valor por defecto

def frase(nombre, apellido,adjetivo = "tonto"):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"
    
frase_resultante = frase("Gonzalo","Gorondona","inteligente")
print(frase_resultante)