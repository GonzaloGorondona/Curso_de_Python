#lista
lista = ["Gonzalo Gorondona " , "Soy Gonzalo ", True, 1.78]
print(lista [0])

#tupla = variable que no se puede modificar
tupla = ("Gonzalo Gorondona " , "Soy Gonzalo ", True, 1.78)

#valido 
lista[3] = "Gonza"

#no valido
#tupla[3]



#creando un conjunto (set) (no pueden haber datos duplicados)
#no se puede acceder por un indice a los elemntos
#datos desordenados

conjunto = {"Gonzalo Gorondona " , "Soy Gonzalo ", True, 1.78}
print(conjunto)

#creando diccionario
#estructura = clave : valor/key : value. Se separa con ,
diccionario = {
    'nombre' : "Gonzalo Gorondona ",
    'canal' : "NateSV",
    'Juega cartitas' : True,
    'altura' : 1.78,
    'dato_duplicado' : "Gonzalo Gorondona"
    
}

print(diccionario['altura'])
print(lista[3])