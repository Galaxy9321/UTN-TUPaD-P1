#Ejercicio 4
edad = int(input("Ingrese su edad: "))
if edad >=0:
    if edad >= 0 and edad < 12:
        print("Niño/a")
    elif edad >= 12 and edad < 18:
        print("Adolescente")
    elif edad >=18 and edad < 30:
        print("Adulto/a Joven")
    elif edad >= 30:
        print("Aduto/a")
else:
    print("No puede ingresar un numero menor que 0")
