#Ejercicio 10

hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("¿Qué número de mes es? (1-12): "))
dia = int(input("¿Qué día del mes es? (1-31): "))
#Estacion del ano segun la fecha introducida
if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    if hemisferio == "N":
        estacion = "Invierno"
    else:
        estacion = "Verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    if hemisferio == "N":
        estacion = "Primavera"
    else:
        estacion = "Otoño"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    if hemisferio == "N":
        estacion = "Verano"
    else:
        estacion = "Invierno"
elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    if hemisferio == "N":
        estacion = "Otoño"
    else:
        estacion = "Primavera"
else:
    estacion = "Fecha inválida"

print(f"Estás en {estacion}.")
