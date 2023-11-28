import os
os.system("cls")

vetor1 = []
vetor2 = []
cont = 0

num = int(input("Insira a quantidade de números que serão inseridos: "))

for i in range(num):
    valores = int(input("Digite um número: "))
    vetor1.append(valores)
while len(vetor1)!=0:
    if vetor1[cont]==max(vetor1): #se vetor1 no indice 0 == num max do vetor1:
        vetor2.append(vetor1[cont]) #vetor2 recebe o valor do vetor1 no indice 0
        vetor1.remove(vetor1[cont]) #vetor1 retira o valor do indice 0
    if cont>=len(vetor1)-1: #se o contador for >= qtd do vetor1 -1
        cont = 0 #contador fica = 0
    else:
        cont+=1 #contador soma +1 pra alcançar os valores do vetor1. caso contrário, ele assume o 1 indice como valor max.
print(vetor2)