#=======================================================================
# QUESTÃO 3

import os
os.system('cls')

def ordenar():

    lista = []

    arquivo = open('questao3.csv', 'a+', encoding='utf-8')
    
    for i in range(6):
        while True:
            
            nomes = input('Digite o nome: ')
            sobrenomes = input('Digite o sobrenome: ')

            arquivo.write(nomes + sobrenomes +'\n')

            if nomes.isalpha() or sobrenomes.isalpha():

                lista.append(f'{nomes} {sobrenomes}')
                break

            else:
                
                print('Digite apenas letras!')
                continue

    lista.sort()
    arquivo.seek(0)
    arquivo.truncate()

    for i in range(len(lista)):

        arquivo.write(lista[i] + '\n')

    arquivo.close()

    return

ordenar()