# -*- coding: utf-8 -*-
import math

nameUser = input("Ingresa tu nombre: ")
lastNameUser = input("\nIngresa tu apellido: ")
foodUser = input("\nIngresa tu comida favorita: ")

phrasePart1 = "Hola, mi nombres es "
phrasePart2 = " y mi comida favorita es "

completePhrase = phrasePart1 + nameUser + " " + lastNameUser + phrasePart2 + foodUser

print("\n" + completePhrase)