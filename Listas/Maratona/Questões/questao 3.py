import os
os.system("cls")

n = int(input("Digite um número: "))

for i in range(1, n+1): # linhas

    for j in range(1,i+1): # coluna
        
        print(j, end=" ")
    print()