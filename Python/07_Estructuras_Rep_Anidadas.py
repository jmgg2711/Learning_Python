# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 18:09:52 2024

@author: jgutierr2

Estructuras de control de iteración anidadas
"""
#region Tablas de multiplicar del 1 al 3
# ---- Ejercicio 1
tblNum = 0
num = 0
while tblNum < 3:
    tblNum += 1
    while num < 10:
        num += 1 
        print(f"{tblNum} x {num} = {tblNum * num}")
    print("\n")
    num = 0    
#endregion

#region Impresion de patron
# ---- Ejercicio 2
val = 6
for i in range(0, val):
    print('.' * (val - i - 1) + '*' * (2 * i + 1))
for j in range(val-2, -1, -1):
    print('.' * (val - j - 1) + '*' * (2 * j + 1))    
#endregion  
