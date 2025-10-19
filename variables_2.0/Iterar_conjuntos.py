animales = {"gato","perro","loro","cocodrilo"}
numeros = {12,56,98,15}

#recorriendo la lista animales

for animal in animales:
    print(f"Ahora la variable animal es igual a: {animal}")
    
#recorriendo la lista numeros y multiplicando cada valor *10


for numero in numeros:
    resultado = numero * 10
    print(resultado)
          
#iterando dos listas del mismo tamaño al mismo tiempo

for numero,animal in zip(animales,numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")
    

for num in range(5,10):
    print(num)
    
#usando el else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual:{numero}")
else:
    print("el bucle terminó")