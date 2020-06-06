# -*- coding: utf-8 -*-

import random
from math import ceil

xPizzas = int(input('Escribe el primer numero: '))
yPizzas = random.randint(1, xPizzas)
zPizzas = xPizzas - yPizzas
horas = random.randint(1,4)

print("\n")
print("--------------------------------------")
print("Lo que sucedio es que teniamos una pizza")
print("con " + str(xPizzas) + " rebanadas y entonces han")
print("venido a comerse " + str(yPizzas) + " rebanadas en")
print("estas " + str(horas) + " horas y por eso ahora quedan")
print("estas rebanadas. En total " + str(zPizzas) + " rebanadas")
print("--------------------------------------")
