#Funciones
def factorial(num):
    
    if num == 1:
        return 1
    else:
        num = num * (factorial(num-1))
    return num

def factoriales_hasta_n(num):
    
    for i in range(1,num+1):
        print(f"El factorial de {i} es: {factorial(i)}")

#Programa principal
num = int(input("Ingrese un numero: "))
factoriales_hasta_n(num)
