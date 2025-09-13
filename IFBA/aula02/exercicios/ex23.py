# 23. Implemente o jogo "Pedra, Papel ou Tesoura". Crie um programa em Python que peça
# ao usuário para escolher e faça uma escolha aleatória para o computador. Imprima o
# vencedor.

from random import choice

from time import sleep


def pedra_papel_tesoura(escolha, escolha_computador):
    if escolha == 'Papel' and escolha_computador == 'Tesoura':
        print('Você perdeu')
        print('---------')
    elif escolha == 'Tesoura' and escolha_computador == 'Pedra':
        print('Você perdeu')
        print('---------')
    elif escolha == 'Pedra' and escolha_computador == 'Papel':
        print('Você perdeu')
        print('---------')
    elif escolha == escolha_computador:
        print('Empate')
        print('---------')
    else:
        print(f'Você ganhou!!! | Sua escolha {escolha} | Computador {escolha_computador}')
        print('---------')
        return True
    return False


while True:
    jogador_computador = choice(['Pedra', 'Papel', 'Tesoura'])
    escolha = str(input('Pedra, Papel, Tesoura: ')).strip().title()
    print('Pedra...')
    print('---------')
    sleep(0.5)
    print('Papel..')
    print('---------')
    sleep(0.5)
    print('Tesoura.')
    pedra_papel_tesoura(escolha, jogador_computador)

    venceu = pedra_papel_tesoura(escolha, jogador_computador)

    if venceu:
        break
