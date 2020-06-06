# -*- coding: utf-8 -*-

value = False
while value != True:
  numUser = input('\nElige un numero del 1 al 6: ')
  try:
    numUser = int(numUser)
    if numUser <=6 and numUser > 0:
      value = True
    else:
      print("\nElige un numero del 1 al 6\n")
  except:
    value = False

if numUser == 1:
  print("Hoy aprenderemos sobre prorgamación")
elif numUser == 2:
  print("¿Qué tal tomar un curso de marketing digital?")
elif numUser == 3:
  print("Hoy es un gran día para comenzar a aprender de diseño")
elif numUser == 4:
  print("¿Y si aprendemos algo de negocios online?")
elif numUser == 5:
  print("Veamos un par de clases sobre producción audiovisual")
elif numUser == 6:
  print("Tal vez sea bueno desarrollar una habilidad blanda en Platzi")