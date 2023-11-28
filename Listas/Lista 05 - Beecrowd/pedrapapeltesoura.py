import os
os.system('cls')

jogo = {'pedra':['lagarto','tesoura'],
        'papel':['pedra','spock'],
        'tesoura':['papel','lagarto'],
        'lagarto':['papel','spock'],
        'spock':['tesoura','pedra']}

#rajesh é o 0 e sheldon é o 1

caso = input().split() # recebe o numero de casos de teste
for i in range(int(caso[0])): # para cada caso de teste (i)
    jogadas = input().split() # recebe as jogadas
    if jogadas[0] in jogo[jogadas[1]]:
        print("sheldon")
    if jogadas[1] in jogo[jogadas[0]]:
        print("rajesh") 
    if jogadas[0] == jogadas[1]:
        print("empate")
    
