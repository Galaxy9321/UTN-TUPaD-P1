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
