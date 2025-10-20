#Digital root is the recursive sum of all the digits in a number.

#Given n, take the sum of the digits of n. 
#If that value has more than one digit, 
#continue reducing in this way until a single-digit number 
#is produced. The input will be a non-negative integer.

def digital_root(n):
    suma_total = 0
    
    for numeros in str(n):
        suma_total += int(numeros)
        
    while suma_total > 9:
        n = suma_total
        suma_total = 0
        for numero in str(n):
            suma_total += int(numero)
    return suma_total
    
print(digital_root(66743563880062))