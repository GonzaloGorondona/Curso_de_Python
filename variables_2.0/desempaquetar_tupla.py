numeros = 12,57,98,15

for indice,num in enumerate(numeros):
    if (num % 2 == 0):
        print(f"el valor de {indice} es {num} y es par")
    elif (num % 2 != 0):
        print(f"el valor de {indice} es {num} y es impar")
else:
    print("fin del bucle")