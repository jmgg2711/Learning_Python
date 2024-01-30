# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 18:23:36 2024

@author: jgutierr2
"""

mi_tupla = 'hola',      # to declare a tupla require comma at the end of the declaration

mi_tupla = ('Hola')     # this is a string

mi_tupla = ('HOLA',)    # 

print(type(mi_tupla))


#region Actividad_4
# ---- Actividad_4_01152024

# 1
nombre = 'Juan'
print(nombre)

# 2: Tipos numéricos
edad = int(47)
print(type(edad))
print(edad)

altura = float(1.75)
print(type(altura))
print(altura)

numero_complejo = complex(3+5j)
print(type(numero_complejo))
print(numero_complejo)

# 3: Tipos de secuencia
colores = ['rojo', 'verde', 'azul']     # lista de colores
print(type(colores))
print(colores)

frutas = ('Manzana', 'Sandia', 'Mandarina')     # tula de frutas
print(type(frutas))
print(frutas)

# Un rango se define de la siguiente forma:
# range(stop): crea un iterador desde 0 hasta el valor de stop agregando 1 en cada iteración
# range(start, stop): crea un iterador desde start hasta stop con paso de 1
# range(start, stop, step): crea un iterador desde start hasta stop con paso step
rango_num = range(1, 6)     # declaración del rango
print(type(rango_num))
print(list(rango_num))

# 4 Tipos de mapeo, Diccionario
informacion_personal = {"Nombre": "Juan", "Edad": 47, "Ciudad": "Tijuana"}
print(type(informacion_personal))
print(informacion_personal)

# 5 Tipos de Conjunto, set y frozenset
vocales = {'a', 'e', 'i', 'o', 'u'}
print(type(vocales))
print(vocales)

meses = {'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre','Diciembre'}
meses = frozenset(meses)
print(type(meses))
print(meses)

# 6 Tipo booleano (bool)
es_python_divertido = True
print(type(es_python_divertido))
print(es_python_divertido)

# 7 Tipos binarios (bytes, bytearray, memoryview)
datos_bytes = bytes([0x4A,0x55,0x41,0x4E])
print(type(datos_bytes))
print(datos_bytes)

b_arr = bytearray([104,111,108,97])  # ASCII en decimal
print(b_arr)

vista_memoria = memoryview(b_arr)
print(vista_memoria)

# 8 Tipo Nulo (NoneType)
variable_nula = None
print(type(variable_nula))
print(variable_nula)


