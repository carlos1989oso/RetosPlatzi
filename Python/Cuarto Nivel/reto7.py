# -*- coding: utf-8 -*-

import math

def perimetroCuadrado(num1):
  return num1 + num1 + num1 + num1

def perimetroRectangulo(num1, num2):
  return num1 + num1 + num2 + num2

def perimetroTriangulo(num1, num2, num3):
  return num1 + num2 + num3

value = False
while value != True:
  print("\n--------------------------------------")
  print("\nBienvenido elige un numero del 1 al 3")
  print("\n1. Perimetro del cuadrado")
  print("\n2. Perimetro del rectangulo")
  print("\n3. Perimetro del triangulo")
  print("\n0. Para salir")

  value2 = False
  while value2 != True:
    print("--------------------------------------")
    num1 = input("\nIngresa tu eleccion: ")
    try:
      num1 = int(num1)
      value2 = True
    except:
      value2 = False

  print("--------------------------------------")
  if num1 == 1:
    value3 = False
    while value3 != True:
      num2 = input("\n¿Cual es el largo del cuadrado?: ")
      try:
        num2 = float(num2)
        value3 = True
      except:
        value3 = False

    print("\nEl perimetro es: " + str(perimetroCuadrado(num2)))
  elif num1 == 2:
    value3 = False
    while value3 != True:
      num2 = input("\n¿Cual es el largo del rectangulo?: ")
      try:
        num2 = float(num2)
        value3 = True
      except:
        value3 = False

    value3 = False
    while value3 != True:
      num3 = input("\n¿Cual es el ancho del rectangulo?: ")
      try:
        num3 = float(num3)
        value3 = True
      except:
        value3 = False

    print("\nEl perimetro es: " + str(perimetroRectangulo(num2, num3)))
  elif num1 == 3:
    value3 = False
    while value3 != True:
      num2 = input("\n¿Cual es un lado del triangulo?: ")
      try:
        num2 = float(num2)
        value3 = True
      except:
        value3 = False

    value3 = False
    while value3 != True:
      num3 = input("\n¿Cual es el siguiente lado del triangulo?: ")
      try:
        num3 = float(num3)
        value3 = True
      except:
        value3 = False

    value3 = False
    while value3 != True:
      num4 = input("\n¿Cual es el siguiente lado del triangulo?: ")
      try:
        num4 = float(num4)
        value3 = True
      except:
        value3 = False

    print("\nEl perimetro es: " + str(perimetroTriangulo(num2 , num3, num4)))
  elif num1 == 0:
    value = True
