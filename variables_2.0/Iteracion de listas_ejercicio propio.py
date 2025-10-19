personas = ["Gonzalo","Delia","Magali","Agustin"]
edades = ["32","71","29","10"]
gustos = ["invierno","primavera","verano", "otoño"]

for persona,edad,estacion in zip(personas,edades,gustos):
    print(f"Se llama {persona}")
    print(f"Y tiene {edad} años")
    print(f"Su estación favorita es {estacion}")