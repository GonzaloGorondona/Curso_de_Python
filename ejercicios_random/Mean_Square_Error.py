#Complete the function that
#accepts two integer arrays of equal length
#compares the value each member in one array to the corresponding member in the other
#squares the absolute value difference between those two values
#and returns the average of those squared absolute value difference between each member pair.

def solution(array_a, array_b):
    diferencia = zip(array_a,array_b)
    suma = 0
    for a,b in diferencia:
        suma += (a - b)**2
    
    resultado = suma /len(array_a)
        
    return resultado
print (solution([10, 20, 10, 2], [10, 25, 5, -2]))