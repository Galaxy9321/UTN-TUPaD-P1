#Ejercicio 10
numero = input("Ingresa un numero: ")
numero_invertido = ""
for i in range(len(numero)-1, -1, -1):
    numero_invertido = numero_invertido + numero[i]
print("El numero invertido es:", numero_invertido)
