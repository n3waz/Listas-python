semana = {}
dias = ["segunda", "terca", "quarta", "quinta", "sexta"]

for i in dias:
    materia = input(f"Qual as materias de {i}? ")
    semana[i] = materia.split(", ")

print(semana)