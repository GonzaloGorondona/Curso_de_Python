#creando una funcion simple
def saludar():
    print("Hola Lucas mi maestro, como andas?")
    
#ejecutando la funcion simple
saludar()

#crear una funcion que tenga parametros
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "titan"
    else:
        adjetivo = "helicoptero apache"
    print(f"Hola {nombre}, {adjetivo}, como andas?")

saludar("Gonzalo","hombre")

#crear funcion que nos retorne multiples valores
def crear_contraeña_random(num):
    chars = "abdkjsieñjdi2315914257s85ebxs9e"
    num_entero = str(num)
    num = int(num_entero[0])
    char1 = num - 2
    char2 = num
    char3 = num - 5
    contraseña = f"{chars[char1]}{chars[char2]}{chars[char3]}{num*2}"
    num * 2
    return(contraseña,num)
    
#desempaquetando la funcion mostrando los datos obteniedos y los datos utilizados para obtenerlo
password, primer_numero = crear_contraeña_random(585)

print(f"Tu contraseña nueva es: {password}")
print(f"El numero utilizado para tu contraseña fue {primer_numero}")
    