#le pedimos al ususario que diga una frase (o varias)
frase = input("Decime una frase y te calculo cuanto tardarías si tuvieras que decirlo ")

#creamos una lista con todas las palabras de la frase (se separan cada vez que haya un espacio en blanco)
palabras_separadas = frase.split(" ")

#usamos len() para ver la cantidad de elementos que hay en la lista
cantidad_de_palabras = len(palabras_separadas)

#en caso de que tarde mas de un minuto en decirlo, le decimos que pare un poco
if cantidad_de_palabras > 120:
    print("Para loco, tremendo discurso")

#calculamos cuanto tardaria en decirlo y se lo decimos
print(f"Dijiste {cantidad_de_palabras} palabras, y tardarías {cantidad_de_palabras/2} segundos en decirlo")
print(f"Dalto lo diría en {cantidad_de_palabras/2*0.7} segundos en decirlo")

