# -*- coding: utf-8 -*-

value = False
while value != True:
  edadUser = input('\n¿Cuantos años tienes: ')
  try:
    edadUser = int(edadUser)
    value = True
  except:
    value = False

if edadUser >= 30:
  print("Nunca es tarde para aprender ¿Qué curso tomaremos?")
elif edadUser < 29 and edadUser >= 18:
  print("Es un momento excelente para impulsar tu carrera.")
elif edadUser > 0 and edadUser < 18:
  print("¿Sabes hacia dónde dirigir tu futuro? Seguro puedo ayudarte.")
else:
  print("Ni siquiera has nacido")