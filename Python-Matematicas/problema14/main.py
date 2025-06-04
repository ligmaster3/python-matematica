#Crear un programa que lea un angulo x en radianes y clcules 10 aproximaciones de sen x por medio de la serie de Taylor.

#formula: senx =sin(x)= 
n=0
# Serie de Taylor para sen(x):
# sen(x) = x - x**3/3! + x**5/5! - x**7/7! + ... + ((-1)**n)*(x**(2n+1))/(2n+1)!


import math
print("\n" + "="*40)
print("  Aproximación de sen(x) usando la serie de Taylor")
print("-----------------------------------------")
x = float(input("Introduce el ángulo x en radianes: "))
print("-----------------------------------------")
terms = 10
taylor_result = 0

for n in range(terms):
    term = ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
    taylor_result += term

actual_result = math.sin(x)
error = abs(actual_result - taylor_result)
print("\n" + "="*40)
print(f"Serie de Taylor: sen({x}) ≈ {taylor_result:.10f}")
print(f"Valor real (math.sin): {actual_result:.10f}")
print(f"Error: {error:.10f}")
print("Fórmula usada: sen(x) = Σ_{n=0}^∞ (-1)^n x^{2n+1}/(2n+1)!")
print("Número de términos usados:", terms)
print("\n" + "="*40)