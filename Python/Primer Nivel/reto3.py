# -*- coding: utf-8 -*-

CATEGORIES = ['Desarrollo e Ingenieria','Diseño y UX', 'Marketing','Negocios y emprendimiento','Producción Audiovisual','Crecimiento Profesional']

print ("Platzi cuenta con cursos de:\n")
for i in range (len(CATEGORIES)):
  print("-- " + CATEGORIES[i] + "\n")