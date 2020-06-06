# -*- coding: utf-8 -*-

def sumatoriaNum(num1, num2):
  return (num1 + num2)

print("Bienvenido a la calculadora\n")
num1 = float(input('Escribe el primer numero: '))
num2 = float(input('Escribe el segundo numero: '))
total = round(sumatoriaNum(num1,num2),2)
print("\n")
print("El resultado de sumar " + str(round(num1,2)) + " mas " + str(round(num2,2)) + " es: " + str(total))
