#Ejercicio 7

#Excluyendo el numero dado por el usuario
num = int(input("Ingrese un numero: "))
sumador = 0
for i in range(0,num):
    sumador = sumador + i
print("El resultado de la suma de los numeros comprendidos entre 0 y ", num, "es: ", sumador)

#Incluyendo el numero dado por el usuario
num = int(input("Ingrese un numero: "))
sumador = 0
for i in range(0,num+1):
    sumador = sumador + i
print("El resultado de la suma de los numeros comprendidos entre 0 y ", num, "es: ", sumador)
