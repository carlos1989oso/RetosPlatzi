# -*- coding: utf-8 -*-

value = False
while value != True:
  num1 = input("\nIngresa un numero: ")
  try:
    num1 = float(num1)
    value = True
  except:
    value = False

value = False
while value != True:
  num2 = input("\nIngresa un numero: ")
  try:
    num2 = float(num2)
    value = True
  except:
    value = False

print("\nEl resultado de la multiplicación es: " + str(round(num1 * num2,2)))