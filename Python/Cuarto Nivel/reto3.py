# -*- coding: utf-8 -*-

value = False
while value != True:
  num1 = input("\nIngresa un numero mayor a 20: ")
  try:
    num1 = float(num1)
    if num1 >= 20:
      value = True
    else:
      print("\nEl numero debe se mayor a 20\n")
      value = False
  except:
    value = False

print("\nEl resultado de la multiplicación es: " + str(round(num1 ** 2,2)))
