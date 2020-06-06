# -*- coding: utf-8 -*-

constNum = 0

def checkAnswer(answer):
  if answer == "si":
    return True
  else:
    return False

def contestacion(answer, constNum):
  valor = checkAnswer(answer)
  if valor == False:
    constNum = 1
  if valor == False and constNum == 1:
    print("\nTen un bonito dia")
  elif valor == True:
    value2 = False
    while value2 != True:
      answer2 = input("\n¿Esta haciendo aire?: ")
      try:
        answer2 = answer2.lower()
        if answer2 == "si" or answer2 == "no":
          value2 = True
      except:
        value2 = False
    valor2 = checkAnswer(answer2)

  if valor == True and valor2 == True:
    print("\nHace mucho aire para salir con un paraguas")
  elif valor == True and valor2 == False:
    print("\nLlevate un paraguas por si las dudas")

value = False
while value != True:
  answer = input("¿Esta lloviendo?: ")
  try:
    answer = answer.lower()
    if answer == "si" or answer == "no":
      value = True
  except:
    value = False

contestacion(answer,constNum)