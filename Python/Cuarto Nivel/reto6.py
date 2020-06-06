# -*- coding: utf-8 -*-

import math

value = False
while value != True:
  num1 = input("\nIngresa el numero 1: ")
  try:
    num1 = float(num1)
    value = True
  except:
    value = False

value = False
while value != True:
  altura = input("\nIngresa el numero 2: ")
  try:
    altura = float(altura)
    value = True
  except:
    value = False

total = int(num1 / altura)
sobrante = int(num1 % altura)

print("\n" + str(int(num1)) + " dividido entre " + str(int(altura)) + " es " + str(total) + " y sobra " + str(sobrante))