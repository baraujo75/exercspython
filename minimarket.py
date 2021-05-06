from time import sleep

val_carrinho = 40

while True:
    print(f'Valor carrinho: {val_carrinho}')
    print('===========================================')
    print('========= Welcome to Bshop ================')
    print('===========================================\n')

    print('Escolha opção abaixo:')
    print('1 - Listar produtos')
    print('2 - Ver carrinho')
    print('3 - Pagar')
    print('4 - Sair')

    option: int = int(input())

    if option == 1:
        print('===========================================')
        print('1 adicionar Playstation 4 no carrinho 3000')
        print('2 adicionar Xbox One no carrinho 2800')
        print('3 adicionar Nintendo Switch no carrinho 1400 ')
        print('4 adicionar Atari no carrinho 6000')
        print('5 Retornar ao menu principal')
        print('============================================')

        option: int = int(input())

        if option == 1:
            val_carrinho += 3000
            print('Playstation adicionado por 3000!')
            print(val_carrinho)
            sleep(2)

        elif option == 2:
            val_carrinho += 2800
            print('Xbox One adicionado por 2800!')
            sleep(2)

        elif option == 3:
            val_carrinho += 1400
            print('Nintendo Switch adicionado por 1400!')
            sleep(2)

        elif option == 4:
            val_carrinho += 6000
            print('Atari adicionado por 6000!')
            sleep(2)

        elif option == 5:
            print('Menu principal!')
            sleep(2)

        else:
            sleep(2)
            print('Opção inválida!')


    elif option == 2:
        print('Valor do carrinho:')
        print(val_carrinho)
        print('Escolha opção abaixo:')
        print('1 - Esvaziar carrinho')
        print('2 - Retornar ao menu')

        option: int = int(input())

        if option == 1:
            val_carrinho = 0
            print('Carrinho esvaziado!')
            print('Valor do carrinho: ')
            print(val_carrinho)

        else:
            print('Retornando ao menu!')
            sleep(2)

    elif option == 3:
        print('Fazer pagamento.')
        val_carrinho = 0
        print(f'Valor carrinho: {val_carrinho}')
        sleep(2)


    elif option == 4:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida!')
