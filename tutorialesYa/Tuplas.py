'''
Created on 9 abr. 2020
  
@author: Knut Waale

'''
print("El programa solicitara que cargues el nombre de 5 empleados")
print("Arrojara los datos cargados y nos dira cuantos empleados ganan mas de 1500")
print()
def cargaEmpleoSueldo():
#Muestra: empleados = [('Car', 1000, 1500, 200), ('Luis', 200, 500, 600), ('Ped', 2040, 2020, 2016), ('Jose', 300, 2400, 2323), ('Antonio', 1050, 1030, 1055)]
    empleados = []
    for i in range(5):
        nombre = input("Carga el nombre de un empleado son 5 llevas " + str(i+1) + ": ")
        sueldo1 = int(input("Sueldo 1: "))
        sueldo2 = int(input("Sueldo 2: "))
        sueldo3 = int(input("Sueldo 3: "))
        print()
        datosEmpleado = (nombre, sueldo1, sueldo2, sueldo3)
        empleados.append(datosEmpleado)
    return empleados


def totalEmpleado(lista):
    totalSueldo = 0
    listaTup = []
    for i in range(len(lista)):
        totalSueldo = lista [i][1] + lista [i][2] + lista [i][3]
        tupAux = (lista[i][0],totalSueldo)
        listaTup.append(tupAux)
    return listaTup
# Se pasa una lista con tuplas adentro, con un str(Nombre) y 3 integer(Sueldos), devuelve otra
#otra lista con tuplas con el nombre y el sueldo totalizado.

def sueldosMayores1500(lista):
# Muestra listaTup [('Car', 2700), ('Luis', 3120), ('Ped', 6076), ('Jose', 5023), ('Antonio', 3135)]
    for i in range(len(lista)):
        if lista[i][1] > 1500:
            print("Empleado Supera 1500: ", lista[i])
        else:
            print("Empleado no Supera 1500: ", lista[i])
        

sueldosMayores1500(totalEmpleado(cargaEmpleoSueldo()))


    