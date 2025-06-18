#un reloj A suena cada N de horas y otro reloj B suena cada M de horas. crear un programa que responda la preguna ¿cuando coincidiran en sonido despues de haya sonado por primera vez? tanto n como m son enteros que se leean  por teclado. el programa debe mostrar la cantidad de horas que transcurriran hasta que coincidan en sonido.
print("-----------------------------------------")
print("Bienvenido al Reloj de Sonido")
print("-----------------------------------------")
n = int(input("Ingrese la cantidad de horas que suena el reloj A: "))
m = int(input("Ingrese la cantidad de horas que suena el reloj B: "))
horas = 1
for i  in range(1,min(n, m) + 1):
    if n % i == 0 and m % i == 0:
        horas = i
print("-----------------------------------------")
print(f"El reloj A suena cada {n} horas y el reloj B suena cada {m}.")
print(f"Los relojes coincidirán en sonido después de {horas} horas.")
print("-----------------------------------------")
#