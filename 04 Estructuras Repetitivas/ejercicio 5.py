#Ejercicio 5
import random
cont = 1
num_ramdon = random.randint(0,9)
num_usu = int(input("Trata de adivinar el numero de 0 a 9 en los menores intentos posibles: "))

while num_ramdon != num_usu:
    cont = cont + 1
    num_usu = int(input("Fallaste, intentalo de nuevo: "))

print("Fueron necesarios ", cont, "intentos.")
