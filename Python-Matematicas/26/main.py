alimentos = ["bistek", "Pan", "Huevo", "Leche", "Avena"]  # alimentos para desayunar
calorias = [272, 265, 155, 42, 68]  # calorías por 100 gramos

print("Opciones de alimentos para desayuno:")
for i, alimento in enumerate(alimentos):
    print(f"{i+1}. {alimento} ({calorias[i]} cal/100g)")

seleccion = []
total_calorias = 0

for i in range(4):
    opcion = int(input(f"Elige el alimento #{i+1} (1-{len(alimentos)}): ")) - 1
    seleccion.append(alimentos[opcion])
    total_calorias += calorias[opcion]

print(f"Has elegido: {', '.join(seleccion)}")
print(f"Calorías totales del desayuno: {total_calorias}")