frutas = ["banana", "manzana", "naranja", "pera", "limon", "mandarina", "uva"]
citricos = ["naranja", "limon", "mandarina"]

for fruta in frutas:
    if fruta in citricos:
        continue
    print(f"Me voy a comer una {fruta} porque no es un cítrico")