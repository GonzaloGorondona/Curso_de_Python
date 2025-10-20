while True:
    try:
        numero1 = int(input("Ingrese el primer numero "))
        numero2 = int(input("Ingrese el segundo numero "))
        resultado = numero1 / numero2
        print(f"el resultado es {resultado}") 
        break
    except Exception:
        print("Ocurrio un error inesperado")

    finally:
        print("Fin del ejercicio")
