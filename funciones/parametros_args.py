#forma no optima de sumar valores

#def suma(lista):
 #   numeros_sumados = 0
 #   for numero in lista:
  #      numeros_sumados = numeros_sumados + numero
   # return numeros_sumados
#resultado = suma(5,3)

#forma optima de sumar valores
def suma_total(numeros):
    return sum(*numeros)

resultado2 = suma_total ([4,5,6,7])

print(resultado2)


#lo mismo de arriba pero utilizando el operador * como argumento args

def suma(nombre,*numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"    

resultado = suma ("Gonzalo", 4,5,6,7) 