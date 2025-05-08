#Ejercicio 9
sumador = 0 
media = 0
for i in range(100):
    num = int(input("Ingrese numeros enteros: "))
    sumador = sumador + num
    media = media + 1

media = sumador / media

print("La media de los valores es: ", media)
