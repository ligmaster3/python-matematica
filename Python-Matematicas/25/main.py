
import random
ciudades = ["Ciudad de Panamá", "Penonomé", "Colón", "David", "Chitré", "Las Tablas", "Santiago"]
salarios = [1288, 500, 550, 600, 450, 400, 500]

print("Ciudades disponibles:")
for i, c in enumerate(ciudades, 1):
    print(f"{i}. {c}")
print("0. Elegir ciudad al azar")
print("==============================================")

opcion = input("\nSeleccione una opción: ")

if opcion == "0":
    idx = random.randint(0, len(ciudades) - 1)
    print(f"Ciudad seleccionada al azar: {ciudades[idx]}")
    print(f"Salario: {salarios[idx]}")
elif opcion.isdigit() and 1 <= int(opcion) <= len(ciudades):
    idx = int(opcion) - 1
    print(f"Ciudad seleccionada: {ciudades[idx]}")
    print(f"Salario: {salarios[idx]}")
else:
    print("Opción inválida.")