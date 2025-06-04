print("-----------------------------------------")
print("| Problema 12 2025 :)")
print("-----------------------------------------")
prodt1 = input("Ingrese el nombre de primer Producto: ")
num1 = float(input("Ingrese el precio de primer Producto: "))
print("-----------------------------------------")
prodt2 = input("Ingrese el nombre de segundo Producto: ")
num2 = float(input("Ingrese el precio de segundo Producto: "))
print("-----------------------------------------")
prodt3 = input("Ingrese el nombre de tercer Producto: ")
num3 = float(input("Ingrese el precio de tercer Producto: "))  

ibtm = 7 / 100
subtotal = num1 + num2 + num3
iva = subtotal * ibtm
total = subtotal + iva
print("-----------------------------------------")
print(f"|                 Resultado        |")
print("-----------------------------------------")
print(f"|  Producto 1: {prodt1} | {num1:.2f}")
print(f"|  Producto 2: {prodt2} | {num2:.2f}")
print(f"|  Producto 3: {prodt3} | {num3:.2f}")
print("-----------------------------------------")
print(f"|      El IVA es: {iva:.2f}            |")
print("-----------------------------------------")
print(f"|      El subtotal es: {subtotal:.2f}  |")
print(f"|      El total es: {total:.2f}        |")
print("-----------------------------------------")