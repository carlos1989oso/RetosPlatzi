# -*- coding: utf-8 -*-
import math

value = False
while value != True:
  numMayor = input('\nEscribe un numero:')
  try:
    numMayor = int(numMayor)
    value = True
  except:
    value = False

value2 = False
while value2 != True:
  numMenor = input('\nEscribe otro numero: ')
  try:
    numMenor = int(numMenor)
    value2 = True
  except:
    value = False

if numMayor > numMenor:
  print("\nEl numero " + str(numMayor) + " es mayor que " + str(numMenor) + " y su diferencia es: " + str(numMayor - numMenor))
elif numMayor == numMenor:
  print("\nLos numeros son iguales")
elif numMenor > numMayor:
  print("\nEl numero " + str(numMenor) + " es mayor que " + str(numMayor) + " y su diferencia es: " + str(numMenor - numMayor))