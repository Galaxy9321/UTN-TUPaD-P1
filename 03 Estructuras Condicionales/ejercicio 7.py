#Ejercicio 7
caracteres = input("Ingrese una frase o palabra: ")
if caracteres[-1].lower() in "aeiou":
    print(caracteres,"!")
else:
    print(caracteres)
