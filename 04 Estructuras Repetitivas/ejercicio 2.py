#Ejercicio 2
dig = int(input("Ingrese un numero entero para saber cuantos digitos tiene: "))
contador = 0
if dig == 0:
    contador = 1
else:
    while dig > 0:
        dig = dig // 10
        contador += 1

print("La cantidad de digitos es:",contador)
