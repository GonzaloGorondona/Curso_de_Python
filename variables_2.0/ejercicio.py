def calcularOperacion(n,m,operador):
    if operador == '+':
        return(n+m)
    elif operador == '-':
        print(n-m)
    elif operador == '/':
        print(n/m)
    elif operador == '*':
        print(n*m)
    else:
        print("operacion fallida")

resuelto = calcularOperacion (calcularOperacion(1,1,"+"),5,"=")

print(resuelto)
