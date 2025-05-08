#Ejercicio 9
mag_terremoto = int(input("Ingrese la magnitud del terremoto: "))
if mag_terremoto < 3:
    print("Muy leve (Imperceptible)")

elif mag_terremoto >= 3 and mag_terremoto < 4:
    print("Leve (Ligeramente perceptible)")

elif mag_terremoto >= 4 and mag_terremoto < 5:
    print("Moderado (Sentido por personas, pero generalmente no causa daños)")

elif mag_terremoto >= 5 and mag_terremoto < 6:
    print("Fuerte (Puede causar daños en estructuras debiles)")

elif mag_terremoto >= 6 and mag_terremoto < 7:
    print("Muy fuerte (Puede causar danos significativos)")

elif mag_terremoto >= 7:
    print("Extremo (Puede causar graves danos a gran escala)")
