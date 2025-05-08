#Ejercicio 4
sumador = 0
cont = 1
num = int(input("Ingrese numeros enteros para saber su suma: "))

while num != 0:
    sumador = sumador + num
    cont = cont + 1
    num = int(input("Ingrese numeros enteros para saber su suma(Con 0 se detiene): "))

print("El total acumulado es: ", sumador)
