#Crear un programa que calcule las componentes horizontales y verticales de un vector en un plano a partir de su módulo cuya magnitud y angulo son ingresados por el usuario, usando funciones trigonometricas del modulo math.
import math
print("-----------------------------------------")
magnitud = float(input("Ingrese la magnitud del vector: "))
angulo = float(input("Ingrese el ángulo del vector : "))

angulo_rad = math.radians(angulo)

vertical = magnitud * math.sin(angulo_rad)
horizontal = magnitud * math.cos(angulo_rad)

print("-----------------------------------------")
print(f"| Componente vertical: {vertical:.2f} |")
print(f"| Componente horizontal: {horizontal:.2f} |")
print("-----------------------------------------")