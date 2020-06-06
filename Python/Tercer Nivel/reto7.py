# -*- coding: utf-8 -*-

from array import array

VOCALES = ['A', 'E', 'I', 'O','U', 'a', 'e','i','o','u']
CONSONANTES = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','Y','Z','b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','y','z']

def separateWords(texto):
  separateWord = " "
  return texto.split(separateWord)

  print(wordsFusion)
  return wordsFusion


def checkWord(word):
  for i in range (len(VOCALES)):
    if word[0] == VOCALES[i]:
      return "Vocal"

  for i in range(len(CONSONANTES)):
    if word[0] == CONSONANTES[i]:
      return "Consonante"

def changeWord(word, valor):
  if valor == "Vocal":
    word = word + "way"
  elif valor == "Consonante":
    word = word[1:] + word[0] +"ay"

  return word

print("----------------------------------------")
textUser = input("\nIngresa un texto: ")

listWords = separateWords(textUser)
texto = ""
for i in range(0,len(listWords)):
  valor = checkWord(listWords[i])
  listWords[i] = changeWord(listWords[i],valor).title()
  if i == len(listWords):
    texto = texto + listWords[i]
  else:
    texto = texto + listWords[i] + " "

texto = texto.capitalize()

print("\n" + texto)




