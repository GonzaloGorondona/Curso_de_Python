def count_bits(n):
    return bin(n)[2:].count('1') 
print(count_bits(1234))