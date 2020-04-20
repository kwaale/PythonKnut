'''
Created on 26 mar. 2020

@author: Knut Waale
'''

notaAlumno = int(input("Introzuca Nota: "))

def evaluacion (nota):
    valoracion = "Aprobado"
    if nota<5:
        valoracion = "Suspenso"
    return valoracion


print(evaluacion(notaAlumno))


