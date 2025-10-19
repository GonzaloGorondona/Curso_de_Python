try:
    numero = int(input("Ingrese un número: "))
    resultado = 10 / numero
    
except ValueError:
    print("Error. Entrada invalida. Ingrese un numero ") 
except ZeroDivisionError:
    print ("No se puede dividir entre cero ")
else:
    print(F"el resultado es {resultado}")
finally:
    print("Fin del programa")  
        

    
