'''
Created on 26 mar. 2020

@author: Knut Waale
'''
from random import random

x = 0
suma = 0


for i in range(1000):
    #x = int(random() * 10)
    x = x + 1
    
    if (x != 2) and (x % 2 == 0) or (x % 5 == 0):
        print(x)
    else:
        print("Primo: " + str(x))
