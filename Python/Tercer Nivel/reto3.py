# -*- coding: utf-8 -*-
import math

value = False
while value != True:
  print("Escribe una oracion de 10 o mas caracteres")
  print("----------------------------------------")
  phrase = input("\nIngresa tu frase de 10 caracteres o mas: ")
  lenPhrase = len(phrase)
  if lenPhrase >= 10:
    value = True

value = False
while value != True:
  print("\n----------------------------------------")
  numMenor = input("\nDigita un numero entre 1 y " + str(lenPhrase) + ": ")
  try:
    numMenor = int(numMenor)
    value = True
  except:
    value = False

value = False
while value != True:
  print("\n----------------------------------------")
  numMayor = input("\nDigita un numero entre " + str(numMenor) + " y " + str(lenPhrase) + ": ")
  try:
    numMayor = int(numMayor)
    if numMayor > numMenor:
      value = True
  except:
    value = False

print("\nEl fragmento de tu frase es: \n")
print(phrase[numMenor - 1 :numMayor])