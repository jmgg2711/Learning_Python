# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 20:02:42 2024

@author: jgutierr2

Práctica 1
Código que genera RFC y CURP
"""
#region Diccionarios
# ---- Diccionarios

# Códigos de estados o entidades federativas
estados_Dict = {"1": "AS", "2": "BC", "3": "BS", "4": "CC", "5": "CL", "6": "CM", 
                "7": "CS", "8": "CH", "9": "DF", "10": "DG", "11": "GT", "12": "GR",
                "13": "HG", "14": "JC", "15": "MC", "16": "MN", "17": "MS", "18": "NT",
                "19": "NL", "20": "OC", "21": "PL", "22": "QT", "23": "QR", "24": "SP", 
                "25": "SL", "26": "SR", "27": "TC", "28": "TS", "29": "TL", "30": "VZ",
                "31": "YN", "32": "ZS", "33": "NE"
           }
# Códigos para género de personas
genero_Dict = {"1": "H", "2": "M"}
#endregion

#region Funciones
# ---- Funciones
def buscaVocal(cadena):
    pos = 0
    for vocal in cadena:
        if vocal in "AEIOU":
            v = cadena[pos]      
            break
        else:
            pos += 1 
    return v
    
def buscaConsonante(cadena):
    pos = 0
    for consonante in cadena:
        if consonante in "BCDFGHJKLMNPQRSTVWXYZ":
            c = cadena[pos]     
            break
        else:
            pos += 1
    return c

def eliminaEspacios(cadena):
    nuevaCadena = ""
    for car in cadena:
        if car != " ":
            nuevaCadena += car
    return nuevaCadena

def fechaDia():
    valido = True
    while True:
        dia = input("Día: ")
        valido = dia.isalnum()
        if valido == True:
            if int(dia) < 1 or int(dia) > 31:
                valido = True
                print("ERROR: día inválido")
            elif int(dia) > 0 and int(dia) < 10:
                dia = dia.zfill(2)
                return dia
            
# def apellidoPaterno():
#     condicion = True
    
#     while True:
#         aPaterno = input("-- Apellido Paterno: ")
#         aPaterno = eliminaEspacios(aPaterno)
        
#         # valido = aPaterno.isalpha()
        
        
        
    #     if len(aPaterno) < 1:
    #         condicion = True
    #         print("ERROR: capture la información requerida")
    #     elif valido == False:
          
    #     if valido == False:
    #         condicion = True
    #         print("ERROR: no es una entrada alfanumérica")
    
    # return aPaterno    
            
#endregion

print("***** Introduce la siguiente información:")

#print('** Apellido paterno: ')
#aPaterno = input()
# aPaterno = apellidoPaterno()
# aPaterno = aPaterno.upper()
# aPaterno = eliminaEspacios(aPaterno)
# c1 = aPaterno[0]                    # CURP y RFC 1er caracter
# c2 = buscaVocal(aPaterno[1:])           # CURP y RFC 2do caracter
# c14 = buscaConsonante(aPaterno[1:])     # CURP 14vo caracter
    
# print('** Apellido materno: ')
# aMaterno = input()
# aMaterno = aMaterno.upper()
# c3 = aMaterno[0]                    # CURP y RFC 3er caracter
# c15 = buscaConsonante(aMaterno[1:])     # CURP 15vo caracter

# print('** Nombre: ')
# nombre = input()
# nombre = nombre.upper()
# c4 = nombre[0]                      # CURP y RFC 4to caracter
# c16 = buscaConsonante(nombre[1:])       # CURP 16vo caracter
# print()

print("** Fecha de nacimiento: ")


# print("** Día de nacimiento: ")
# dia = input()
# dia = int(dia)
# if dia > 0 and dia < 9:
#     dia = dia.zfill(2)
# elif dia < 1 or dia > 31:
dia = fechaDia()
c9_10 = str(dia)                   # CURP y RFC digitos 9 y 10 dia

print("** Mes de nacimiento: ")
mes = input()
c7_8 = str(mes)                   # CURP y RFC digitos 7 y 8 mes

print("** Año de nacimiento: ")
anio = input()
anio = str(anio)
c5_6 = anio[2:]                   # CURP y RFC digitos 5 y 6 año
print()

print("***** Entidad de nacimiento:")
print("""1. AGUASCALIENTES             18. NAYARIT     
2. BAJA CALIFORNIA            19. NUEVO LEON
3. BAJA CALIFORNIA SUR        20. OAXACA
4. CAMPECHE                   21. PUEBLA
5. COAHUILA                   22. QUERETARO
6. COLIMA                     23. QUINTANA ROO
7. CHIAPAS                    24. SAN LUIS POTOSI
8. CHIHUAHUA                  25. SINALOA
9. DISTRITO FEDERAL           26. SONORA
10. DURANGO                   27. TABASCO
11. GUANAJUATO                28. TAMAULIPAS
12. GUERRERO                  29. TLAXCALA
13. HIDALGO                   30. VERACRUZ
14. JALISCO                   31. YUCATAN
15. MEXICO                    32. ZACATECAS
16. MICHOACAN                 33. NACIDO EN EL EXTRANJERO
17. MORELOS""")
print("** Selección: ")
entidad = input()
entidad = str(entidad)
c12_13 = estados_Dict[entidad]      # CURP digitos 12 y 13
print()

print("***** Seleccione género:")
print("""1. Hombre
2. Mujer""")
print("** Selección: ")
genero = input()
genero = str(genero) 
c11 = genero_Dict[genero]           # CURP digito 11vo

rfc = c1 + c2 + c3 + c4 + c5_6 + c7_8 + c9_10
curp = rfc + c11 + c12_13 + c14 + c15 + c16 

 # salida = f"CURP: {curp} \n RFC: {rfc}"
# print(f"CURP1: {curp} \n RFC1: {rfc}")
# print(f"\nCURP2: {c1}{c2}{c3}{c4}{c5_6}{c7_8}{c9_10}{c11}{c12_13}{c14}{c15}{c16}\n RFC2: {c1}{c2}{c3}{c4}{c5_6}{c7_8}{c9_10}")