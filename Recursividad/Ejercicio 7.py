#Funciones

def contar_bloques(num):
    
    if num == 0:
        return num
    else:
        num = num + (contar_bloques(num - 1))
    return num
        
    
#Programa principal

num = int(input("Ingrese la cantidad de bloques del nivel mas bajo: "))
print(f"El total de bloques que se necesita es: {contar_bloques(num)}")
