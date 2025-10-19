animales = ["gato","perro","loro","cocodrilo"]

#recorriendo la lista animales

for animal in animales:
    print(f"Ahora la variable animal es igual a: {animal}")
    
#recorriendo la lista numeros y multiplicando cada valor *10

numeros = [12,56,98,15]
for numero in numeros:
    resultado = numero * 10
    print(resultado)
          
#iterando dos listas del mismo tamaño al mismo tiempo

for numero,animal in zip(animales,numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")
    
#forma no optima de recorrer una lista
for num in range(len(numeros)):
    print(numeros[num])

for num in range(5,10):
    print(num)
    
#forma correcta de recorrer una lista por su indice 
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es: {indice} y el valor es: {valor}")
    
#usando el else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual:{numero}")
else:
    print("el bucle terminó")