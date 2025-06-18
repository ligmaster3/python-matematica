#una floristeria reciben rosas y m calvales, donde n y m enteros positivos que se leasn por teclado. la  florsteria queir  hacer ramos con la mayor cantidad posible de flores de cada tipo.crear un programa responda a la pregunta: ¿cuantos ramos de flores se pueden poner para que  tods los ramso sean iguales?
print("-----------------------------------------")
print("Bienvenido a la Floristería")
print("-----------------------------------------")

n = int(input("Ingrese la cantidad de rosas: "))
m = int(input("Ingrese la cantidad de claveles: "))

menor = min(n, m)
ramos = 1
for i in range(1, menor + 1):
    if n % i == 0 and m % i == 0:
        ramos = i
print("" + "-" * 40)
print(f"Se pueden hacer {ramos} ramos iguales.")
