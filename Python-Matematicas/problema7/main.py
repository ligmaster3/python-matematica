import math # inportacino de una libreria para calcular las variables de la esfera

print("-----------------------------------------")
print("| Problema 7 2025 :)")
print("-----------------------------------------")
#CREAR  un programa que lea el radio de una esfera y que calcule y presente en pantalla su volumen y superficie. de dicha esfera.
print("|  Calcular volumen y superficie de una esfera   |")


radio = float(input("Ingrese el radio de la esfera: "))
volumen = (4/3) * math.pi * (radio ** 3)
superficie = 4 * math.pi * (radio ** 2)

print("\n" + "=" * 45)
print(f"RESULTADOS PARA RADIO = {radio} m")
print("=" * 45)
print(f"→ Volumen:    {volumen:.4f} m³")
print(f"→ Superficie: {superficie:.4f} m²")
print("=" * 45)