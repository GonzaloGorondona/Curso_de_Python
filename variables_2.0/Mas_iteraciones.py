frutas = ["banana", "manzana", "ciruela","pera","naranja","granada","durazno"]
cadena = "Hola Gonzalo"
numeros = [5,9,8,7]

#evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta == "manzana":
        continue
    print(f"me voy a comer una {fruta}")
    
#evitar que el bucle siga ejecutandose
for fruta in frutas:
    if fruta == "pera":
        break
    print(F"me voy a comer una {fruta}")
    
#recorrer una cadena de texto

for letra in cadena:
    print(letra)
    
#for en una sola linea de codigo (duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)