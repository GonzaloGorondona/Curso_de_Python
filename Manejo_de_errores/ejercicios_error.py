while True:
    try:
        numero = int(input("Ingrese un numero "))
        resultado = 10 / numero
        print(F"el resultado es {resultado}")
    except ValueError:
        print("Error. Entrada invalida. Ingrese un numero ")
    except ZeroDivisionError:
        print ("No se puede dividir entre cero ")
    else:
        print(resultado)
        break

    

    
    