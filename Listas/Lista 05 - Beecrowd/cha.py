import os
os.system('cls')

cont = 0 # contador de acertos
cha = int(input()) # recebe a resposta do cha
competidores = input().split() # recebe as respostas dos competidores

for i in range(len(competidores)):
    if int(competidores[i]) == cha:
        cont += 1
print(cont)

