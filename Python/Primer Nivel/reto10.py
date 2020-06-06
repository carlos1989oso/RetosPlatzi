# -*- coding: utf-8 -*-

import math 

millasUser = float(input('\n¿Cuantas millas quieres convertir a kilometros?: '))

kmUser = 1.609344 * millasUser

print("\n\nEn " + str(round(millasUser,2))  + " millas hay " + str(round(kmUser,2)) + " kilometros")

