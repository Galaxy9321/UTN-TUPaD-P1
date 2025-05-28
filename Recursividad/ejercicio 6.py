#Funciones

def suma_digitos(n):
    
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)
        
#Programa principal
num = int(input("Ingrese numero: "))
print(suma_digitos(num))
