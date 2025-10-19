usuario = "Pepe Pape"
contraseña = "Pepe123"

usuario_correcto = "Pepe Papo"
contraseña_correcta = "Pepe123"

if usuario == usuario_correcto:
    print("Ingrese su contraseña")
else:
    print("Usuario incorrecto")
    
if contraseña == contraseña_correcta:
        print("Autenticando")
else:
        print("Contraseña incorrecta")
        
if contraseña_correcta == contraseña and usuario_correcto == usuario:
    print("Iniciando sesión")
else:
    print("Usuario o contraseña incorrectas")
    
if input