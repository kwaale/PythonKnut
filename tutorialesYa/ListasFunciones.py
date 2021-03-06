'''
Created on 9 abr. 2020
  
@author: Knut Waale

Ordena listas. Mayo, Menor
'''
from random import random
miLista = []
mayor = 0
for i in range(10):
    miLista.append(int(random()*10))
#Determina el Mayor de la Lista
def mayor(lista):
    mayor = 0
    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
    return mayor

#Determina el Menor
def menor(lista):
    menor = 0
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    return menor       
#Suma de la lista
def sumaLista(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma

#Ordena lista de mayor a menor
def ordenaListaMay(lista):
    aux = 0
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[j] < lista[j + 1]:
                aux = lista[j + 1]
                lista[j + 1] = lista[j]
                lista[j] = aux
    return lista

#Ordena lista de menor a mayor
def ordenaListaMen(lista):
    aux = 0
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[j] > lista[j + 1]:
                aux = lista[j + 1]
                lista[j + 1] = lista[j]
                lista[j] = aux
    return lista

print("Original: ",miLista)
print("Mayor de la lista: ", mayor(miLista))
print("Menor de la lista: ", menor(miLista))
print("Sumatoria: ",sumaLista(miLista))
print("Orden Mayor a Menor: ", ordenaListaMay(miLista))
print("Orden Menor a Mayor: ", ordenaListaMen(miLista))