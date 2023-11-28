import os
os.system("cls")

matriz = [[],[],[]]
media = []
soma = 0

#for para adicionar os valores da tabela:
for l in range(3): #linhas
  for c in range(3): #colunas
    matriz[l].append(int(input(f"Informe os valores na sequência: Salário médio, tempo mínimo de experiência e valor da carga horária: ")))

#for para mostrar os valores da tabela:
for l in range(3):
  for c in range(3):
    print(f"[{matriz[l][c]:^4}]", end = " ")

    if l == c:
      soma += matriz[l][c]
  print()


print(f"A média dos salários é igual a {(sum(matriz[0]))/3}") #Média dos salários
print(f'A soma dos valores na diagonal é igual a {soma}') #Soma das diagonais