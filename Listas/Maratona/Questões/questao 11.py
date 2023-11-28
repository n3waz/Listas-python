cont = 0
sum = 0

while True:
    idade = int(input("Digite a idade: "))
    cont+=1
    sum+=idade
    if idade == 999:
        break

print(f"Média das idades: {sum/cont}")
print(f"Quantidade de alunos: {cont}")
