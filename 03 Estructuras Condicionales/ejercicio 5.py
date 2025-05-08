#Ejercicio 5
contra = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
if len(contra) >= 8 and len(contra) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
