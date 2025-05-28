#Funciones
def segundos_a_hora(seg):
    seg = seg/3600
    print(f"La cantidad de horas es: {seg}")

#Programa principal

seg = int(input("Ingresa los segundos: "))
segundos_a_hora(seg)
