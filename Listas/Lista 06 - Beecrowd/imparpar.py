import os 
os.system("cls") 
p, j1, j2, r, a = input().split()

resultado = (int(j1) + int(j2)) % 2 # soma os números e verifica se é par ou impar

def jogo(p, j1, j2, r, a):
    if((r == '1') and (a == '1')): # se os dois trapacearem [AND]
        print('Jogador 2 ganha!') # jogador 2 ganha

    elif((r == '1') or (a == '1')): # se um trapacear [OR]
        print('Jogador 1 ganha!') # jogador 1 ganha

    else:
        if(resultado == 0): # se a soma for par
            if(p == '1'): # se o jogador 1 escolher par
                print('Jogador 1 ganha!') # jogador 1 ganha
            else:
                print('Jogador 2 ganha!') # jogador 2 ganha
        elif(resultado == int(p)): # se a soma for impar e o jogador 1 escolher impar
            print('Jogador 2 ganha!') # jogador 2 ganha
        else:
            print('Jogador 1 ganha!') # jogador 1 ganha
    return # retorna o resultado
 
jogo(p, j1, j2, r, a) # chama a função jogo
