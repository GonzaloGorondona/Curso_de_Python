def conversor():
    try:
        temperatura_del_usuario = float(input("Ingrese una temperatura a convertir: "))
    except ValueError:
        return "Error: Debe ingresar un número válido."
    tipo_de_temperatura = input("Es Farenheit(F) o Celsius(C)?: ").lower()
    C = (temperatura_del_usuario - 32) / 1.8
    F = temperatura_del_usuario * 1.8 + 32
    
    if tipo_de_temperatura == "c":
        return F
    elif tipo_de_temperatura == "f":
        return C
    else:
        return "Ingrese c o f"
    

print(conversor())