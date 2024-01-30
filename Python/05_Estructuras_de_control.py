# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 18:23:23 2024

@author: jgutierr2

Imprimir si un alumno está aprobado según su calificación (aprobará solo si es mayor a 60).
"""
#region If
# ---- Ejercicio-1
print("Captura calificación: ")
calif = input()
calif = int(calif)
if calif > 60:
    print("aprobado")
#endregion

#region If-Else
# ---- Ejercicio-2
print("Captura A: ")
a = int(input())
print("Captura B:")
b = int(input())
if a > 2 and b > 2:
    print(f"a: {a} y b: {b} son mayores que 2")
else:
    print(f"a: {a} y b: {b} NO son mayores que 2")
#endregion

#region If-Elif
# ---- Ejercicio-3
num = int(input("Ingresa un número: "))
if num > 0 :
    print(f"{num} es positivo")
elif num == 0:
    print(f"{num} es cero")
else: 
    print(f"{num} es negativo")
#endregion

#region Convertidor numero a texto
# ---- Ejercicio-4
numLetrasDict = {"1": "uno", "2": "dos", "3": "tres", "4": "cuatro", "5": "cinco"}
num = input("Captura un número de 1 a 5: ")
if num in numLetrasDict:
    num = int(num)
    print(f"{num} - {numLetrasDict[str(num)]}")
#endregion

#region Ordenar ascendente
# ---- Ejercicio-5
a = int(input("Captura 1er número: "))
b = int(input("Captura 2do número: "))
c = int(input("Captura 3er número: "))
if a < b:
    if a < c:
        if b < c:
            print(f"El orden es {a}, {b}, {c}")
elif b < c:
    if a < c:
        print(f"El orden es {b}, {a}, {c}")
else:
    print(f"El orden es {b}, {c}, {a}")
#endregion

#region Dias de la semana
# ---- Ejercicio-6
diasSemanaDict = {"1": "Lunes", "2": "Martes", "3": "Miercoles", "4": "Jueves", "5": "Viernes", "6":"Sábado", "7":"Domingo"}
numDia = input("Captura el número de día de la semana: ")
if numDia in diasSemanaDict:
    numDia = int(numDia)
    print(f"{numDia} - {diasSemanaDict[str(numDia)]}")
else:
    print("error")
#endregion
    