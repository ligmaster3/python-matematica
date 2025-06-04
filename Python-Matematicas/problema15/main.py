#En cierto pais, los varones se jubilan a los 62 años de edad y las mueres a los 60 años.
#sin embargo, los que se dedican a la educacion pueden pagar un plan de retiro anticipado(P.R.A.A), el cual les permite retirarse 5 años antes de los normal y percibir durante su carrera (usualmente el ultimo salario), luego de transcurridos esos 5 años, los educacdores se unen al resto de los jubilados y empiezan a percibir el 60% de su mejor salario. Suponiendo que tanto hombres como mujeres empiezan percibiendo un salario de 575.00 mensual, y que cada 5 años reciben un aumento de 35.00. Crear un programa que lea el nombre, el sexo y la edad de inicio en el sistema de un educador y calcule e imprima.
#.los años que le faltan para jubilarse y retirarse con el P.R.A.A.
#.el salario al final de su carrera.
#lo que percibira durante los 5 años de vigencia del P.R.A.A.
#lo que percibirar despues de expirara el PRA


def calcular_jubilacion():
    nombre = input("|  -Ingrese el nombre del educador: ")
    sexo = input("|  -Ingrese el sexo (M/F): ").strip().upper()
    edad_inicio = int(input("|  -Ingrese la edad de inicio en el sistema: "))

    # Determinar edad de jubilación según el sexo
    if sexo == 'M':
        edad_jubilacion = 62
    elif sexo == 'F':
        edad_jubilacion = 60
    else:
        print("Sexo no válido.")
        return

    # Calcular edad de retiro con Plan de Retiro Anticipado (PRAA)
    edad_retiro_praa = edad_jubilacion - 5
    anios_para_retirarse = edad_retiro_praa - edad_inicio

    # Cálculo de salario
    salario_inicial = 575.00
    aumento_cada_5 = 35.00
    anios_trabajados = edad_retiro_praa - edad_inicio
    aumentos = anios_trabajados // 5
    salario_final = salario_inicial + (aumentos * aumento_cada_5)

    # Salarios durante PRAA y después
    salario_praa = salario_final
    salario_post_praa = salario_final * 0.6
     
    # Imprimir resultados
    print("\n--- RESULTADOS ---")
    print(f"\nEducador: {nombre}")
    print("-----------------------------------------")
    print(f"Años que le faltan para jubilarse con el P.R.A.A.: {anios_para_retirarse}")
    print("-----------------------------------------")
    print(f"Salario al final de su carrera: ${salario_final:.2f}")
    print("-----------------------------------------")
    print(f"Lo que percibirá durante los 5 años de vigencia del P.R.A.A.: ${salario_praa:.2f} mensual")
    print("-----------------------------------------")
    print(f"Lo que percibirá después de expirar el P.R.A.A.: ${salario_post_praa:.2f} mensual")
    print(f"\n")
    print("-----------------------------------------")

# Ejecutar la función principal
if __name__ == "__main__":
    calcular_jubilacion()
