#declarar y definir variables

nombre = "Gonzalo "
apellido = "Gorondona "

#concatenar con +

bienvenido = "hola " + nombre + "como estás?"
print(bienvenido)

#definiendo variable con snake_case

nombre_apellido = nombre+apellido
print(nombre_apellido)
#concatenar con f strings

bienvenido =f"Hola {nombre}"
print(bienvenido)

#operadores de pertenencia (in y not in)

print("Gonzalo" in bienvenido) #true
print("Ezequiel" not in bienvenido) #true
print("Gonzalo" not in bienvenido) #false