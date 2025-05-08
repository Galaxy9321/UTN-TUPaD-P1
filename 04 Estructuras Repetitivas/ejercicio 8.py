#Ejercicio 8

pos = 0
neg = 0
par = 0
impar = 0

for i in range(100):
    num = int(input("Ingrese numero entero: "))
    if num % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1
    if num > 0:
        pos = pos + 1
    else:
        neg = neg + 1
    

print("Pares: ", par)
print("Impares: ", impar)
print("Negativos: ", neg)
print("Positivos: ", pos)
