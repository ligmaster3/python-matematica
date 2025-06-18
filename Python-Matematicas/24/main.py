

print("-----------------------------------------")

estudiantes = ["luis", "maria", "pedro", "jose", "marcos", "exa", "jaimito"]
notas = [4.0, 4.4, 4.9, 3.9, 3.4, 5.0, 4.0]

# Mostrar la lista de estudiantes con su índice
for i, estudiante in enumerate(estudiantes):
    print(f"{i} - {estudiante}")

nombre = input("Ingrese el nombre del estudiante: ").lower()


if nombre in estudiantes:
    indice = estudiantes.index(nombre)
    nota = notas[indice]
    print("-----------------------------------------")
    print(f"La nota de {nombre} es: {nota}")