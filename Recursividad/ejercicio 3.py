#Funciones
def potencia(n,m):
    if m == 0:
        return 1
    else:
        return n * potencia(n,m-1)
        
#Programa principal
n  = int(input("Ingrese su numero de base: "))
m = int(input("Ingrese su numero de exponente: "))
print(f"El resultado es: {potencia(n,m)}")
