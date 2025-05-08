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

#Ejercicio 7
caracteres = input("Ingrese una frase o palabra: ")
if caracteres[-1].lower() in "aeiou":
    print(caracteres,"!")
else:
    print(caracteres)

#Ejercicio 8
nombre = input("Ingrese su nombre: ")
print("1. Su nombre en mayuscula")
print("2. Su nombre en minuscula")
print("3. Su nombre con la primera letra en mayuscula")
caso = input("Ingrese la opcion deseada: ")
if caso == "1" or caso == "2" or caso == "3":
    if caso == "1":
        print(nombre.upper())
    elif caso == "2":
        print(nombre.lower())
    elif caso == "3":
        print(nombre.title())
else:
    print("Ingrese una opcion valida")

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

