#Ejercicio 1
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

#Ejercicio 2
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio 3
num = int(input("Ingrese un numero par: "))
if num % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")

#Ejercicio 4
edad = int(input("Ingrese su edad: "))
if edad >=0:
    if edad >= 0 and edad < 12:
        print("Niño/a")
    elif edad >= 12 and edad < 18:
        print("Adolescente")
    elif edad >=18 and edad < 30:
        print("Adulto/a Joven")
    elif edad >= 30:
        print("Aduto/a")
else:
    print("No puede ingresar un numero menor que 0")

#Ejercicio 5
contra = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
if len(contra) >= 8 and len(contra) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6
from statistics import mode,median,mean
import random
# No entendi si hay que imprimir los numeros por pantalla, pero las lineas de los prints de los numero aleatorios estan comentadas
numeros_aleatorios = [random.randint(1,100) for i in range (50)]
if mean(numeros_aleatorios) > median(numeros_aleatorios) and median(numeros_aleatorios) > mode(numeros_aleatorios):
    print("Sesgo positivo")
    #print(numero_aleatorios)
elif mean(numeros_aleatorios) < median(numeros_aleatorios) and median(numeros_aleatorios) < mode(numeros_aleatorios):
    print("Sesgo negativo")
    #print(numeros_aleatorios)
elif mode(numeros_aleatorios) == median(numeros_aleatorios) == mean(numeros_aleatorios):
    print("Sin sesgo")
    #print(numeros_aleatorios)

