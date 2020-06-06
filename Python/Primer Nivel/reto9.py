# -*- coding: utf-8 -*-

import random
import math 

def daysToHours(days):
  return days * 24

def hoursToMinutes(hours):
  return hours * 60

def minutesToSeconds(minutes):
  return minutes * 60

diasCount = float(input('\n¿Cuantos dias quieres calcular?: '))

hoursCoverted = daysToHours(diasCount)
hoursInt = math.trunc(hoursCoverted)
hoursRes = hoursCoverted - hoursInt

minutesConverted = hoursToMinutes(hoursRes)
minutesInt = math.trunc(minutesConverted)
minutesRes = minutesConverted - minutesInt

secondsConverted = minutesToSeconds(minutesRes)
secondsConverted = math.trunc(secondsConverted)

print("\n\nEn " + str(diasCount)  + " dias hay " + str(hoursInt) + " horas, " + str(minutesInt) + " minutos y " + str(secondsConverted) + " segundos")

