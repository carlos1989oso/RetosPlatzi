# -*- coding: utf-8 -*-
import math

def timesCOunt(numMayor, numMenor):
  return numMayor / numMenor

value = False
while value != True:
  numMayor = input('\nEscribe un numero mayor a 1000: ')
  try:
    numMayor = int(numMayor)
    if numMayor > 1000:
      value = True
    else:
      print("\nEscribe un numero mayor a 1000\n")
  except:
    value = False

value2 = False
while value2 != True:
  numMenor = input('\nEscribe un numero menor a 100: ')
  try:
    numMenor = int(numMenor)
    if numMenor < 100 and numMenor > 0:
      value2 = True
    else:
      print("\nEscribe un numero menor a 100 y mayor a 0\n")
  except:
    value = False

print("\n")
print("--------------------------------------")
print("Tu numero " + str(numMenor) + " cabe " + str(round(timesCOunt(numMayor,numMenor),2)) + " veces en tu numero mayor " + str(numMayor))
print("--------------------------------------")