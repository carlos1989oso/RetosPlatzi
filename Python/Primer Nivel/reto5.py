# -*- coding: utf-8 -*-

def sumatoriaNum(num1, num2):
  return (num1 + num2)

def multiNum(num1, num2):
  return (num1 * num2)

print("Bienvenido a la calculadora\n")
num1 = float(input('Escribe el primer numero: '))
num2 = float(input('Escribe el segundo numero: '))
num3 = float(input('Escribe el segundo numero: '))

total = sumatoriaNum(num1,num2)
total = round(multiNum(total,num3),2)


print("\n")
print("El resultado es: " + str(total))