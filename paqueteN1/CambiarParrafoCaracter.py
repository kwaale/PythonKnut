'''
Created on 25 mar. 2020

@author: Knut Waale
'''
elementos = "Los organismos ediacaricos, tambien conocidos como biota del periodo Ediacarico o, anteriormente, biota o fauna vendiense; son antiguas formas"

for i in range(len(elementos)):
    if (elementos[i] == (caracter = " ")):
        elementos.append("a")
    print(elementos[i])

#Un string sustituye espacios por comas
#def sustEspaComa (lista):
#    for i in lista:
#        if i == " ":
#            i = ", "
#    return lista

#print(sustEspaComa(elementos))