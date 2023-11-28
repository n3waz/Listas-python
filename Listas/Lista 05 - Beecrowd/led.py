import os
os.system('cls')

leds = {'1':[2],'2':[5],'3':[5],'4':[4],'5':[5],'6':[6],'7':[3],'8':[7],'9':[6],'0':[6]}
soma = 0

num = int(input()) # numero de casos de teste

for valor in range(num):
    valor = input()
    for i in valor:
        soma += leds[i][0]
    print(soma,"leds")
    soma = 0
