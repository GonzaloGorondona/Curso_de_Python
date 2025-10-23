#Complete the solution so that the function will break 
#up camel casing, using a space between words.

def solution(s):
    resultado = ""
    for letras in s:
        if letras.isupper():
            resultado += (" ")+letras
        else: 
            resultado += letras
    return resultado
       
print (solution("camelCase"))
    