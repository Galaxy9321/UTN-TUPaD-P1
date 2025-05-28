#Funciones
def numero_validado(mensaje,min = float("-Inf"),max = float("Inf")):
    num = int(input(f"{mensaje}: "))
    while num < min or num > max:
        num = int(input(f"Error. {mensaje}: ")) 
    return num

def binario(num):
    if num == 0:
        return ""
    elif num == 1:
        return "1"
    else:
        return binario(num // 2) + str(num % 2)# str(num % 2) concatena con lo anterior como si fuera una cadena de texto
    
#Programa principal
num = numero_validado("Ingrese un numero entero positivo",1)
print(f"El numero en binario es: {binario(num)}")
