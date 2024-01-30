# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 18:48:10 2024

@author: jgutierr2
"""
lista_nombres = ["Juan", "Martha", "Oscar", "Laura", "Araceli"]

def BuscaNombre(nombre):
    for nom in lista_nombre:
        if nombre == nom:
            print("Si se encontró")
            break
        else:
            print("No se encontró")
            
entrada = input("Captura nombre a buscar: ")

BuscaNombre(entrada)
