'''
Created on 25 mar. 2020

@author: Knut Waale
'''
# Declarar Diccionario
miDiccionario = {"Alemania" : "Berlin", "Francia" : "Paris", "Inglaterra" : "Londres", "Espana" : "Madrid"}
print(miDiccionario["Alemania"])

# Agregar Valor al diccionario
miDiccionario["Italia"]="Roma"
print(miDiccionario)

#Eliminar Vaor del Diccionario
del miDiccionario["Francia"]
print(miDiccionario)

#Tupla para dar varlor al diccionario
miTupla = ["Espana", "Francia", "Inglaterra", "Alemania"]
miDiccionario2 = {miTupla[0] : "Madrid", miTupla[1] : "Paris", miTupla[2] : "Londres", miTupla[3] : "Berlin"}
print(miDiccionario2)

#Imprimir valor valro de una clave
print(miDiccionario2["Francia"])

#Guardar una Tupla dentro de un diccionario
miDiccionario3 = {23:"Jordan", "Nombre":"Michael", "Equipo" : "Chicago", "Anisllos":[1990,1991,1992,1993]}
print(miDiccionario3)

#Diccionario dentro de un diccionario
miDiccionario4 = {23:"Jordan", "Nombre":"Michael", "Equipo" : "Chicago", "Anisllos":{"Temporadas":[1990,1991,1992,1993]}}
print(miDiccionario4)

#Traer claves / Valores / Longitud diccionario
print(miDiccionario4.keys())
print(miDiccionario4.values())
print(len(miDiccionario4))