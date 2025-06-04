# Una empresa exporta 3 productos distintos: piña, melón y sandía.
# Cada tonelada métrica de piña genera una ganancia de 735.75,
# cada tonelada de melón 443.50 y cada tonelada de sandía 276.95.
# El programa debe leer un pedido internacional de toneladas métricas de cada producto,
# calcular e imprimir la ganancia bruta y la ganancia neta (el estado cobra un 8.5% de impuestos sobre la ganancia bruta).
# El programa debe seguir calculando pedidos hasta que las tres cantidades sean cero.

PIÑA_GANANCIA = 735.75
MELON_GANANCIA = 443.50
SANDIA_GANANCIA = 276.95
IMPUESTO = 0.085

print("-----------------------------------------")
print("Ingrese las toneladas métricas de piña, melón y sandía.")
print("\n" + "="*40 + "\n")

while True:
    try:
        piña = float(input("Ingrese toneladas métricas de piña: "))
        melon = float(input("Ingrese toneladas métricas de melón: "))
        sandia = float(input("Ingrese toneladas métricas de sandía: "))
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
        continue

    if piña == 0 and melon == 0 and sandia == 0:
        print("\n--- Programa Finalizado ---")
        break

    ganancia_bruta = (piña * PIÑA_GANANCIA) + (melon * MELON_GANANCIA) + (sandia * SANDIA_GANANCIA)
    impuesto = ganancia_bruta * IMPUESTO
    ganancia_neta = ganancia_bruta - impuesto

    # Mostrar resultados
    print("\n--- RESUMEN DE VENTAS ---")
    print(f"Toneladas de Piña:   {piña:.2f} | Ganancia: ${PIÑA_GANANCIA:.2f}")
    print(f"Toneladas de Melón:  {melon:.2f} | Ganancia: ${MELON_GANANCIA:.2f}")
    print(f"Toneladas de Sandía: {sandia:.2f} | Ganancia: ${SANDIA_GANANCIA:.2f}")
    print("\n--- RESUMEN FINANCIERO ---")
    print(f"Ganancia Bruta:      ${ganancia_bruta:.2f}")
    print(f"Impuestos (8.5%):    ${impuesto:.2f}")
    print(f"Ganancia Neta:       ${ganancia_neta:.2f}")
    print("\n" + "="*40 + "\n")