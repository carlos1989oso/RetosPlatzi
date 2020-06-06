# -*- coding: utf-8 -*-

import math

value = False
while value != True:
  numMayor = input('\nEscribe un limite superior:')
  try:
    numMayor = int(numMayor)
    value = True
  except:
    value = False

value2 = False
while value2 != True:
  numMenor = input('\nEscribe un limite inferior: ')
  try:
    numMenor = int(numMenor)
    value2 = True
  except:
    value = False

value2 = False
while value2 != True:
  numeroAsk = input('\nEscribe un numero: ')
  try:
    numeroAsk = int(numeroAsk)
    value2 = True
  except:
    value = False

if numeroAsk > numMayor:
  print("\nEl número " + str(numeroAsk) + " excede el límite permitido")
elif numeroAsk < numMenor:
  print("\nEl número " + str(numeroAsk) + " no alcanza el límite permitido")
elif numeroAsk >= numMenor and numeroAsk <= numMayor:
  print("\nEl número " + str(numeroAsk) + " se encuentra en el rango, gracias")