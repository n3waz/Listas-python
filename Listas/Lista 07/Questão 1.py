#=======================================================================
# QUESTÃO 1

import os
os.system("cls")

lista = []

maiores = 0
menores = 0
iguais = 0

for i in range(1, 11):
    while True:
        try:
            lista.append(int(input('Insira números inteiros: ')))
        except:
            print('Insira apenas números inteiros!')
            pass
        else:
            break

for j in range(len(lista)):

    if j > 0:
        if lista[j] > lista[0]:
            maiores+=1
        elif lista[j] < lista[0]:
            menores+=1
        else:
            iguais+=1

print('A quantidade de elementos maiores que o Primeiro é: ', maiores)
print('A quantidade de elementos menores que o Primeiro é: ', menores)
print('A quantidade de elementos iguais ao Primeiro é: ', iguais)