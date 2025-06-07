#Diccionario dado:
precios_frutas = {"Banana":1200, "Anana":2500, "Melon":3000, "Uva":1450}

#Agregar Frutas con sus respectivos precios:
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

#Actualizacion de precios:
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melon"] = 2800

#Lista sin precios:
frutas_sin_precios = list(precios_frutas.keys())
print(frutas_sin_precios)
