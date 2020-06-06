# -*- coding: utf-8 -*-

import random
from math import ceil

def taxes(totalCount, propina):
  propina = propina / 100
  totalCount = totalCount + (totalCount * propina)
  return totalCount * 1.16

def divideAccount(totalCount, personas):
  return totalCount / personas

cuenta = float(input('¿Cuanto fue?: '))
personas = int(input('\n¿Cuantos somos?: '))
propina = float(input('\n¿Cuando es de propina?: '))

cuenta = taxes(cuenta, propina)
totalPagar = divideAccount(cuenta,personas)
print("\n\nSe debe pagar " + str(round(cuenta,2)) + " en total y nos toca de a " + str(round(totalPagar,2)) + "")

