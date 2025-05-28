#Funciones

def es_palindromo(pal):
    if len(pal) <= 1:
        return True
    if pal[0] != pal[-1]:
        return False
    
    return es_palindromo(pal[1:-1])
        
#Programa principal
pal = input("Ingrese una cadena de texto sin espacios ni tilde: ")
print(es_palindromo(pal))
