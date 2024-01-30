# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 19:45:46 2024

@author: jgutierr2
"""
#region Say_Hello
# ---- Practica 1
def Say_Hello(nombre):
    print(f"Hola {nombre}")

for i in range(3):
    nombre = input("Cual es tu nombre: ")
    Say_Hello(nombre)

#region Ana va realizar su fiesta...
# ---- Ejercicio 1
def Invitados():
    edad = int(input("Captura tu edad: "))
    if edad > 15:
        cadena = "Solo puedes entrar si traes regalo."
    elif edad == 15:
        cadena = "Eres un joven que entra completamente gratis."
    else:
        cadena = "Creo que eres menor, por lo tanto no puedes entrar."
    return cadena

acceso = Invitados()
print(acceso)

#region Convertidor de temperatura
# ---- Ejercicio 2
def C2F(celsius):
    celsius = int(celsius)
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

def C2K(celsius):
    celsius = int(celsius)
    kelvin = celsius + 273.15
    return kelvin

gradoC = input("Grados Celsius: ")
gradosF = C2F(gradoC)
gradosK = C2K(gradoC)
print(f"Celsius -> Fahrenheit: {gradosF}\nCelsius -> Kelvin: {gradosK} ")


# region Empresa de bienes raíces...
# ---- Ejercicio 3
def CalcEnganche(_costo,_ingreso):
    enganche = 0
    costo = float(_costo)
    ingreso = float(_ingreso)
    if ingreso <= 8000:
        enganche = costo * 0.15
        
    else:
        enganche  = costo * 0.30
    return enganche    

def CalcMensualidad(_costo,_ingreso):
    costo =  float(_costo)
    ingreso = float(_ingreso)
    if ingreso <= 8000:
        total = costo - costo * 0.15
        mensualidad = total / (15 * 12)
    else:
        total = costo - costo * 0.30
        mensualidad = total / (7 * 12)
    return mensualidad

ingreso = float(input("Ingreso: "))
costoVivienda = float(input("Costo vivienda: "))

enganche = 0
enganche = CalcEnganche(costoVivienda,ingreso)
mensualidad = 0
mensualidad = CalcMensualidad(costoVivienda, ingreso)

print(f"Enganche: {enganche}")
print(f"Mensualidad: {mensualidad}") 

if ingreso <= 8000:
    meses = 15 * 12
else:
    meses = 7 * 12
    
for i in range(1,meses+1):
    print(f"Mes{i}: {mensualidad}")

