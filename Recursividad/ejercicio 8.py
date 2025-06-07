#Funciones
def contar_digito(num,digito):
    
    if num == 0:
        return num
    elif num % 10 == digito:
        return 1 + contar_digito(num // 10,digito)
    else:
        return contar_digito(num // 10,digito)
    
#Programa principal
num = int(input("Ingrese un numero entero positivo: "))
dig = int(input("Ingrese un digito del 0 al 9: "))
print(f"La cantidad de veces que aparece el numero {dig} es: {contar_digito(num,dig)}")
