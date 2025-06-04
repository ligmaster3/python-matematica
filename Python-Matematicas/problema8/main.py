import math # inportacion de una libreria para calcular las variables del triangulo

print("-----------------------------------------")
print("| Problema 8 2025 :)")
print("-----------------------------------------")
# calcular los tres lados del triangulo y calcular y presente el area de dicho triangulo.
print("|  Calcular area de un triangulo   |")
lado1 = float(input("Ingrese el primer lado del triangulo: "))
lado2 = float(input("Ingrese el segundo lado del triangulo: "))
lado3 = float(input("Ingrese el tercer lado del triangulo: "))
# Calcular el semiperimetro
semiperimetro = (lado1 + lado2 + lado3) / 2
# Calcular el area usando la formula de Heron
area = math.sqrt(semiperimetro * 
                 (semiperimetro - lado1) * 
                 (semiperimetro - lado2) * 
                 (semiperimetro - lado3))
print(f"El area del triangulo es: {area:.2f}")
# Mostrar el resultado
print("-----------------------------------------")
print(f"|  Area del triangulo: {area:.2f}        |")
print("-----------------------------------------")
