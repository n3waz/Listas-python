import os
os.system("cls")

num = int(input("Insira um número natural inteiro não-negativo: "))
i = 1
s = 0
while s < num:
    s = i*(i+1)*(i+2) #atribuindo os números consecutivos na varíavel s
    i+= 1
if s == num:
    print(f'O número {num} é um triângulo.')
else:
    print(f'O número {num} não é um triângulo')