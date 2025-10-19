cadena1 = "Hola soy Gonzalo"
cadena2 = "bienvenido"

#convierte a mayusculas
mayusculas = cadena1.upper()

#convierte a minusculas
minusculas = cadena1.lower()

#primera letra en mayuscula
primer_letra_mayuscula = cadena1.capitalize()

#buscamos una cadena en otra cadena. Si no hay coincidencias devuelve -1
busqueda_find = cadena1.find("H")

#buscamos una cadena en otra cadena. Si no hay coincidencia, lanza una excepción
busqueda_index = cadena1.index("G")

#si es numerico, devolvemos true, sino devolvemos false
es_numerico = cadena1.isnumeric()

#si es alfanumerico, devolvemos true, sino devolvemos false. Los espacios no son alnum
es_alfanumerico = cadena1.isalnum()

#buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincida
contar_coincidencia = cadena1.count("a")

#FUNCION contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve TRUE
empieza_con = cadena1.startswith("Hol")

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve TRUE
termina_con = cadena1.endswith("lo")

#reemplaza un pedazo de la cadena dada por otra dada. Si encuentra una coincidencia, reemplaza.
cadena_nueva = cadena1.replace("la","lu")
cadena_nueva2 = cadena2.capitalize()

#separa cadenas, con la cadena que le pasemos
cadena_separada = cadena1.split (" ")

print(cadena_separada)
