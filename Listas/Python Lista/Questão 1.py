#defeitos:
#1 - necessita da esfera;
#2 - necessita de limpeza;
#3 - necessita troca do cabo ou conector;
#4 - quebrado ou inutilizado

import os
os.system("cls")

defeito = []
esfera = []
limpeza = []
quebrado = []
troca = []
soma = 0

defeito.append(int(input("Informe a quantidade de mouses com defeito: \n")))
esfera.append(int(input("Informe quantos mouses necessitam da esfera: \n")))
limpeza.append(int(input("Insira a quantidade que necessitam de limpeza: \n")))
quebrado.append(int(input("Insira a quantidade de mouses quebrados: \n")))
troca.append(int(input("Informe quantos mouses para troca de Cabo ou Conector: \n")))
print()

soma = limpeza[0] + esfera[0] + quebrado[0] + troca[0]

if soma > defeito[0]:
    print("Dados Inválidos")
else:
    print(f'Quantidade de mouses: {defeito}')

    print(f'Situação\t\t\t\tQuantidade\t\tPercentual')
    print(f'1 - Necessita da Esfera\t\t\t\t{esfera[0]}\t\t{(esfera[0]/defeito[0])*100}%')
    print(f'2 - Necessita de Limpeza\t\t\t{limpeza[0]}\t\t{(limpeza[0]/defeito[0])*100}%')
    print(f'3 - Necessita de Troca de Cabo ou conector\t{troca[0]}\t\t{(troca[0]/defeito[0])*100}%')
    print(f'4 - Quebrado ou Inutilizado\t\t\t{quebrado[0]}\t\t{(troca[0]/defeito[0])*100}%')





