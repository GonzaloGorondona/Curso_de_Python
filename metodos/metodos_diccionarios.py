diccionario = {
    "nombre" : 'Gonzalo',
    "apellido" : 'Gorondona',
    "subs" : '39'
}

#nos devuelve un objeto dict_item
#devuelve el valor de una clave
claves = diccionario.keys()

#obteniendo un elemento con .get() (si no encuentra nada el programa continua)
valor_de_nombre = diccionario.get("nombre")

#elimina todo del diccionario
#diccionario.clear()

#elimina un elemento del diccionario
diccionario.pop("subs")

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()


print(diccionario_iterable)


