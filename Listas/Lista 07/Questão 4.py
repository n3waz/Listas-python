#=======================================================================
# QUESTÃO 4

import os
os.system('cls')

lista_nomes = []

def escrever_nomes():
    nomes = open('questao4.csv', 'w', encoding='utf-8')

    for i in range(6):
        try:
            nome = input('Digite o nome: ')

            if nome.isalpha() == False:
                print('Digite apenas letras!')
                continue

            else:
                nomes.write(nome + '\n')
                lista_nomes.append(nome)

        except:
            print('Digite apenas letras!')
            continue

    os.system('cls')
    nomes.close()

    return

def atualizar_nomes():

    cont = 0
    nomes = open('questao4.csv', 'a+', encoding='utf-8')
    while True:

        for i in range(len(lista_nomes)):

            print()
            print(lista_nomes[i])
            
            try:
                atualizar = input('Deseja atualizar este nome e sobrenome? (S/N) ')
            except:
                print('Digite apenas S ou N!')
                continue

            cont += 1

            if atualizar == 'S' or atualizar == 's':
                try:
                    novo_nome = input('Digite o novo nome: ')
                    lista_nomes[i] = novo_nome
                    nomes.seek(0)
                    nomes.truncate()

                except:
                    print('Digite apenas letras!')
                    continue

                for j in range(len(lista_nomes)):
                    nomes.write(lista_nomes[j] + '\n')

            elif atualizar == 'N' or atualizar == 'n':

                continue

            elif atualizar != 'S' and atualizar != 'N':

                print('Opção inválida!')
                continue

        if cont == len(lista_nomes):

            break
            
    nomes.close()
    print(lista_nomes)

escrever_nomes()
atualizar_nomes()