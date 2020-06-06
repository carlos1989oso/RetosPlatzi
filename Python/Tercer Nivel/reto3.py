# -*- coding: utf-8 -*-
import math

print("Todos los datos deben ser en minusculas")
print("----------------------------------------")
nameUser = input("\nIngresa tu nombre: ")
lastNameUser = input("\nIngresa tu apellido: ")
countryUser = input("\nIngresa tu país: ")

nameUser = nameUser.title()
lastNameUser = lastNameUser.title()
countryUser = countryUser.title()

print("\n" + nameUser + " " + lastNameUser + " es de " + countryUser)