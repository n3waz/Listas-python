def calculo():
    comidas = {'suco de laranja':120, 'morango fresco':85, 'mamao':85, 'goiaba vermelha':70, 'manga': 56, 'laranja':50, 'brocolis':34}
    while True:
        num = int(input())
        if num == 0:
            break

        vitamina = 0
        for i in range(num):

            interacao = input().split()
            qtd = int(interacao[0])
            fruta = ' '.join(interacao[1:])
            vitamina += comidas[fruta]*qtd

        if vitamina < 110:
            print('Mais %d mg' % (110-vitamina))

        elif vitamina > 130:
            print('Menos %d mg' % (vitamina-130))
            
        else:
            print('%d mg' % (vitamina))

calculo()