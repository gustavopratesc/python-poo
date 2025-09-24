# 24. Insira um novo elemento em uma posição específica de uma lista. O usuário informa a
# posição (índice) e o elemento

lista = ['Arroz', 'Macarrao', 'Feijão', 'Carne']

for i, v in enumerate(lista):
    print(f'{i}: {v}')

try:
    posicao = int(input('Insira a posição em que quer mudar de elemento: '))
    elemento = input('Insira o novo elemnto: ').strip().title()
    lista.pop(posicao)
    lista.insert(posicao, elemento)
    print(lista)
except ValueError:
    print('ERRO: Insira apenas números!')