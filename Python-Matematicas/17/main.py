#crear en pantalla u 10 multiplicaciones tomadas de la tabla de multiplicar al azar, para que el usuario escribar por teclado el resultado. Para  cada pregunta, el programa felicitara al usuario si acierta o si falla , le mostrara  la respuesta correcta y un mensaje de animo para que siga practicando.
import random
print("-----------------------------------------")
print("  Practica la tabla de multiplicar")
print("-----------------------------------------")

for i in range(10):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    resouesta = num1 * num2
    user_input = int(input(f"¿Cuánto es {num1} x {num2}  "))
    
    if user_input == resouesta:
        print("¡Correcto! Muy bien hecho.")
       
    else:
        print(f"Has fallado. La respuesta correcta es {resouesta}.")
        print("Sigue practicando, practica hace al maestro")
print("-----------------------------------------")

