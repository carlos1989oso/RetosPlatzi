# -*- coding: utf-8 -*-


print("----------------------------------------")
nameUser = input("\nEscribe tu nombre: ")
lenPhrase = len(nameUser)
if lenPhrase >= 5:
  print("\nHola " + nameUser)
else:
  lastNameUser = input("\nEscribe tu apellido: ")
  print("\nHola " + nameUser + " " + lastNameUser)
