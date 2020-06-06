# -*- coding: utf-8 -*-

import math

value = False
while value != True:
  num1 = input("\nIngresa el radio de un circulo: ")
  try:
    num1 = float(num1)
    value = True
  except:
    value = False

print("\nEl resultado de la multiplicación es: " + str(round(math.pi * (num1 ** 2),2)))
