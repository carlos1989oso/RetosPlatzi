# -*- coding: utf-8 -*-
import math

value = False
while value != True:
  numMayor = input('\nEscribe un limite numerico:')
  try:
    numMayor = int(numMayor)
    value = True
  except:
    value = False

value2 = False
while value2 != True:
  numMenor = input('\nEscribe un numero: ')
  try:
    numMenor = int(numMenor)
    value2 = True
  except:
    value = False

if numMayor >= numMenor:
  print("\nEl número " + str(numMenor) + " se encuentra en el rango, gracias")
elif numMenor > numMayor:
  print("\nEl número " + str(numMenor) + " excede el límite permitido")