num_telefonico = {}
#Pedir los 5 contactos a guardar
for i in range(0,5):
    Nombre = input("Ingrese el nombre del contacto a guardar: ")
    Numero = int(input("Ingrese el numero del contacto a guardar: "))
    print("----------------------------------------")
    num_telefonico[Nombre]= Numero

Nombre = input("Ingrese el Nombre para ver el numero telefonico: ")
#Verificar si existe el nombre en el diccionario:
if Nombre in num_telefonico:
    print(f"El numero telefonico de {Nombre} es: {num_telefonico[Nombre]}")
else:
    print("No existe ese nombre")
