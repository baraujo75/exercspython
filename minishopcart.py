from time import sleep

val_carrinho = 200

while True:
    sleep(2)
    print('Entre opção: ')
    print('1 Esvaziar carrinho')
    print('2 Ver carrinho')
    print('3 Adicionar produto')
    print('4 Sair')

    option: int = int(input())

    if option == 1:
        val_carrinho = 0
        print('Carrinho esvaziado.')
        print(val_carrinho)
        sleep(2)

    if option == 2:
        print(val_carrinho)

    if option == 3:
        val_carrinho += 200

    if option == 4:
        print('Até mais!')
        break
