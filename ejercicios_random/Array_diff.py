#Implement a function that computes the difference between two 
#lists. The function should remove all occurrences of elements 
#from the first list (a) that are present in 
#the second list (b). The order of elements in the first list 
#should be preserved in the result.

def array_diff(a, b):
    resultado = list(a)
    
    for elementos in list(resultado):
        if elementos in b:
            resultado.remove(elementos)
            
    return resultado
print (array_diff([11, -12], [-17, 13, -10, -2, 8]))