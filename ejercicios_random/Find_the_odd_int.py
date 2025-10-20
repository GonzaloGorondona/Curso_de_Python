#Given an array of integers, 
#find the one that appears an odd number of times.
#There will always be only one integer that appears an odd number of times.

def find_it(seq):
    for numero in seq:
        conteo = seq.count(numero)
        if conteo %2 != 0:
            return (numero)
        
print(find_it([0,1,0,1,0])) 