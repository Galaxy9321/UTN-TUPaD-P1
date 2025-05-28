#Funciones
def fibonacci(num):
    
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

def fibonacci_hasta_n(num):
    for i in range(0,num):
        print(fibonacci(i))
        
#Programa principal
num = int(input("Ingrese un numero para ver la sucesion de fibonnaci hasta esa posicion: "))
fibonacci_hasta_n(num)
