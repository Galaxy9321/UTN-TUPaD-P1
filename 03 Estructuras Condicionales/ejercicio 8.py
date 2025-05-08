#Ejercicio 8
nombre = input("Ingrese su nombre: ")
print("1. Su nombre en mayuscula")
print("2. Su nombre en minuscula")
print("3. Su nombre con la primera letra en mayuscula")
caso = input("Ingrese la opcion deseada: ")
if caso == "1" or caso == "2" or caso == "3":
    if caso == "1":
        print(nombre.upper())
    elif caso == "2":
        print(nombre.lower())
    elif caso == "3":
        print(nombre.title())
else:
    print("Ingrese una opcion valida")
