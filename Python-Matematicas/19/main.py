#Crear  un program que leea la cantidad de tiempo en horas en forma decimal, x ejemplo tiempo = 49,55 horas  y que se tranforme en dias, horas y minutos. El programa debe mostrar el resultado en pantalla. usando las metodos del redondeo de math.
import math
print("-----------------------------------------")
tiempo = float(input("Ingrese la cantidad de tiempo en horas: "))
dias = math.floor(tiempo / 24)
horas = math.floor(tiempo % 24)
minutos = math.floor((tiempo - (dias * 24 + horas)) * 60)
print("-----------------------------------------")
print(f"| Días: {dias} |")
print(f"| Horas: {horas} |")    
print(f"| Minutos: {minutos} |")
print("-----------------------------------------")