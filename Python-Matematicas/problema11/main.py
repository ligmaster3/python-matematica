# crear un programa que lear por teclado el largo, el ancho y el espesor de un objeto rectangular y calcule su volumen. El volumen de un paralelepipedo y calcule su superficie y volumne  y que presente ambos resultados en pantalla. 
print("-----------------------------------------")
print("| Problema 11 2025 :)")
print("-----------------------------------------")

# Leer dimensiones
largo = float(input("Ingrese el largo: "))
ancho = float(input("Ingrese el ancho: "))
espesor = float(input("Ingrese el espesor: "))

# Calcular volumen y superficie
volumen = largo * ancho * espesor
superficie = 2 * (largo * ancho + largo * espesor + ancho * espesor)

# Mostrar resultados
print(f"El volumen es: {volumen}")
print(f"La superficie es: {superficie}")
