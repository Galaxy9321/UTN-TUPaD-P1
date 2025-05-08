#Ejercicio 3
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
sumador = 0
for i in range(num1+1,num2):
    sumador = sumador + i

print("La suma de los numeros comprendidos entre los dos valores es: ", sumador)
