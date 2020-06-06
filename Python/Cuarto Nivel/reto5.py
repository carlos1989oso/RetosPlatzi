# -*- coding: utf-8 -*-

import math

value = False
while value != True:
  num1 = input("\nIngresa el radio del cilindro: ")
  try:
    num1 = float(num1)
    value = True
  except:
    value = False

value = False
while value != True:
  altura = input("\nIngresa la altura del cilindro: ")
  try:
    altura = float(altura)
    value = True
  except:
    value = False

total = (math.pi * (num1 ** 2))* altura
total = round(total,2)
print("\nEl resultado de la multiplicación es: " + str(total))