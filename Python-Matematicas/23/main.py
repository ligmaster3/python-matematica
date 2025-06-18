#crear un programa que ofresca una lista de destinos(puede usar los de ejemplos 1) y una lista de precios (investige o invente) para vaiajar a esos destinos. que el usuario escoja tres destinos y el programa le muestre el precio total del viaje, y la suma de los precios de cada destino. el programa debe mostrar el precio total del viaje y la suma de los precios de cada destino.# Agencia de viajes básica usando listas

print("-----------------------------------------")
print("Bienvenido a la Agencia de Viajes")
print("-----------------------------------------")
# Listas paralelas: índices 0-4 corresponden a cada destino
destinos = ["París", "Tokio", "Nueva York", "Barcelona", "Sídney"]
precios = [233, 950, 263, 216, 1015] 

print("\nDestinos disponibles:")
for i in range(len(destinos)):
    print(f"{i + 1}. {destinos[i]} - ${precios[i]}")

# Seleccionar 3 destinos
lugares = []
for i in range(3):
    seleccion = int(input(f"\nSelecciona el destino {i + 1} (1-{len(destinos)}): ")) - 1
    lugares.append(seleccion)

total = sum(precios[l] for l in lugares)

print("\n--- Resumen de tu viaje ---")
print("-----------------------------------------")
for i in lugares:
    print(f"Destino: {destinos[i]} - Precio: ${precios[i]}")
print("-----------------------------------------")
print("Precio total del viaje: $", total)
print("-----------------------------------------")
