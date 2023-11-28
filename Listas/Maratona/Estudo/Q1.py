import os
os.system('cls')

login = {}

cont = 0
pago = 0
pendente = 0

def register():

    global cont
    global pago
    global pendente
    while cont <= 10:
        try:
            usuario = input("Insira o nome: ")
            if usuario == 'sair' or usuario == 'SAIR':
                break
        except:
            print('O nome deve conter apenas letras!')
            continue
        try:
            senha = int(input("Insira a senha: "))
        except:
            print('A senha deve conter apenas números!')
            continue
        try:
            situacao = input('Insira a situação: \nP - Pago \nF - Pendente\n')
            if situacao != 'P' and situacao != 'F':
                print('A situação deve ser P ou F!')
                continue
        except:
            print('A situação deve conter apenas letras!')
            continue
        login[usuario] = [senha, situacao]
        if situacao == 'P':
            pago += 1
            print(f'Seja bem vindo {usuario}! E bom treino! \n')
        if situacao == 'F':
            pendente += 1
            print(f'Não se esqueça de pagar a mensalidade {usuario}! \n')
        if usuario in login == False:
            print('Seja bem vindo! \n')
        cont+=1

register()