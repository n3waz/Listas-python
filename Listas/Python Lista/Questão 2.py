import os
os.system("cls")

vetorA = []
vetorB = []
vetorC = []
par = [] #lista dos pares
imp = [] # lista dos impares
for i in range(5):
    vetorA.append(float(input("Insira um número para o vetor A: ")))
    vetorB.append(float(input("Insira um número para o vetor B: ")))

vetorC = vetorA + vetorB
for n in vetorC: #p = par
    if n % 2 ==0:
        par.append(n)
    if n % 2 !=0:
        imp.append(n)
print(f'A soma dos números pares do Vetor C são: {sum(par)}')    
print(f'A média dos números ímpares do Vetor C são: {(sum(imp)/len(imp)):.2f}')
print(f'O menor valor do Vetor C é: {min(vetorC)}')
        
