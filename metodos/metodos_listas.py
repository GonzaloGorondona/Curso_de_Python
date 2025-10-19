#FUNCION crea una lista
lista = list (["Hola","Gonzalo",32])
lista2 = list ([True,1,6,9,False,85,4])

#devuelve la cantidad de elementos de la lista
cantidad_elementos =len(lista)

#agregando un elemento a la lista
agregando_con_append = lista.append("xD")

#agregando un elemento a la lista en un indice especifico. 
#Cada insert limita a 1 elemento
lista.insert(2,"Aguante Boca")
lista.insert(3,"EOOO")

#agregando varios elementos a una lista
lista.extend(["Pikachu",123])

#eliminar un elemento de la lista por su indice
#Usar numeros negativos (-1,-2) para eliminar elementos a partir del ultimo
lista.pop(0)

#removiendo un elemento de la lista por su valor
lista.remove("Pikachu")

#ordenar elementos de forma ascendente a descendente. 
#False y True en ese orden van primero

lista2.sort()

#invirtiendo los elementos de una lista
lista2.reverse()

#verificando si un elemento se encuentra en una lista
elemento_encontrado = lista.index("Gonzalo")


#eliminar elementos de la lista
print(lista,lista2.clear)

