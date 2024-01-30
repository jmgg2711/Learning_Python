# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 18:10:02 2024

Código que determina si un año es bisiesto

@author: jgutierr2
"""

anio =  2021

if ( anio % 4 == 0 ) and ( anio % 100 != 0 or anio % 400 == 0):
    print('El año %d es bisiesto' % anio)
else: 
    print('El año %d no es bisiesto' % anio)