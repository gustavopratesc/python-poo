perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

# forma sofrida
# print(f'Pergunta: {perguntas[0]["Pergunta"]}')
# print(f'Opções: {perguntas[0]["Opções"]}')
# r = str(input('Insira a sua resposta: '))
# if r == perguntas[0]["Resposta"]:
#     print(f'Você acertou')
# else:
#     print(f'Você errou!')

# forma normal

qtd_acertos = 0

for pergunta in perguntas:
    print(pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for indice, opcao in enumerate(pergunta['Opções']):
        print(f'{indice}){opcao}')
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou!')
    else:
        print('Errou!')


    print()

print(f'Você acertou {qtd_acertos} de {len(perguntas)} perguntas')