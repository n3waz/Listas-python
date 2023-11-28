matrizA = [[],[],[],[]]
matrizB = [[],[],[],[]]
matrizC = [[],[],[],[]]

for i in range(4):
    for j in range(4):
        matrizA[i].append(int(input("Digite um número: ")))

for l in range(4):
    for c in range(4):
        matrizB[l].append(int(input("Digite um número: ")))

for k in range(4):
    for m in range(4):
        matrizC[k].append(matrizA[i][j] + matrizB[l][c])
    
for i in range(4):
    for j in range(4):
        print(f'{matrizC[i][j]}', end=' ')
    print()

