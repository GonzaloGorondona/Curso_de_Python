#Move the first letter of each word to the end of it, 
# then add "ay" to the end of the word. 
# Leave punctuation marks untouched.

def pig_it(text):
    palabras = text.split()
    resultado_palabras = []
    
    for palabra in palabras:
        letras = []
        puntuacion = ""
        for char in palabra:
            if char.isalpha():  
                letras.append(char)
            else:
                puntuacion += char
        
        if letras:
            primer_elemento = letras.pop(0)  
            letras.append(primer_elemento)
            letras.append("ay")              
            palabra_transformada = "".join(letras) + puntuacion  # Reconstruir con puntuación
        else:
            palabra_transformada = palabra
        
        resultado_palabras.append(palabra_transformada)
    
    return " ".join(resultado_palabras)

print (pig_it("Pato Ñato!"))
        