#un cajero automatico solo entrega billetes de 20    y billetes de 5 dolares. el cajero debe tratar de utilizar siempre  de preferencia la mayor cantidad de billees de 20 dolares y la menor cantidad de billetes de 5 dolares.  ejemplo para entregar 95 dolares deberas usar 4 billetes de 20  y 3 billes de 5 dolares. creear un programa que lea por teclado una cantidad de dinero ( que tiene  que ser multiplo de 5 ) el programa debe mostrar el pantalla la cantidad de billetes de 20  nesesarios y la cantidad de 5 dolares nesesario que se entregan. segun el criterio del cajero automatico.
print("-----------------------------------------")
print("Bienvenido!")
print("Cajero Automático")
print("-----------------------------------------")
dinero = int(input("Ingrese la cantidad de dinero (múltiplo de 5): "))
print("-----------------------------------------")

if dinero % 5 != 0 or dinero <= 0:
    print("La cantidad debe ser un número positivo y múltiplo de 5.")
else:
    b20 = dinero // 20
    cantidad = dinero % 20
    b5 = cantidad // 5
    print("-----------------------------------------")
    print(f"| Billetes de 20|: {int(b20)}| ") 
    print(f"| Billetes de 5|: {int(b5)}| ")
    print("-----------------------------------------")
    