#Funciones
def celcius_a_fahrenheit(celcius):
    return celcius * (9/5) + 32

#Programa principal
celcius = float(input("Ingrese una temperatura en Celcius: "))
print(f"La temperatura en Fahrenheit es: {celcius_a_fahrenheit(celcius):.1f}")
