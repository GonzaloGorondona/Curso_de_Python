ingreso_mensual = 2500
gasto_mensual = 1500

#if anidado y else if (elif)

if ingreso_mensual >= 1000:
    if ingreso_mensual - gasto_mensual < 0:
        print ("Se registra déficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print ("Saludable económicamente")
    else:
        print ("Se registran gastos elevados. Tener cuidado")

elif ingreso_mensual > 1000:
    print("Sobre el básico en Argentina")
elif ingreso_mensual > 500:
    print("sobre el básico en Venezuela")
elif ingreso_mensual < 500:
    print("Sos pobre")
    
