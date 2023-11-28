materia = int(input("Digite o número de matérias: "))
sum1 = 0
sum2 = 0

Ira = 0 
for i in range(materia):
    nota = float(input("Digite a nota: "))
    carga_horaria = int(input("Digite a carga horária: "))
    sum1 += nota * carga_horaria

    sum2 += carga_horaria * 100

ira = sum1 / sum2
print(f"O seu IRA é: {ira}")
