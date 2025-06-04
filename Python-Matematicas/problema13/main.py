# Crear un programa que lea por teclado los enteros positivos n, a y b, con a menor que b, y calcule estos valores.
# El programa deberá generar una tabla de valores para la función f(x) = x^n + 2x - 7.
# Dicha tabla deberá comenzar con f(a) y terminar con f(b), mostrando el valor de x y el resultado de la función f(x) para cada valor de x.
print("-----------------------------------------")
print("\n" + "="*40)
print("  Tabla de valores para f(x) = x^n + 2x - 7")
print("="*40)
print("-----------------------------------------")

n = int(input("Introduce el valor de n (entero positivo): "))
a = int(input("Introduce el valor de a (entero positivo): "))
b = int(input("Introduce el valor de b (Mayor que a ): "))
print("-----------------------------------------")

if n <= 0:
    print("Error: n debe ser un entero positivo.")
elif a <= 0:
    print("Error: a debe ser un entero positivo.")
elif b <= a:
    print("Error: b debe ser mayor que a.")
else:
    print(" x\t|\tf(x)")
    print("-"*25)
    for x in range(a, b + 1):
        result = x**n + 2*x - 7
        print(f"{x}\t|\t{result}")
print("-----------------------------------------")