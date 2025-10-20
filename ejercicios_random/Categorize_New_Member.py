def open_or_senior(data):
    resultado = []
    
    for Age,Handicap in data:
        if Age >= 55 and Handicap > 7:
            resultado.append("Senior")
        else:
            resultado.append("Open")
    return resultado
    
print(open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))    
            