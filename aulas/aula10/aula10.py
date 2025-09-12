'''
Função lambda em Python
A função lambda é uma função como qualquer outra em Python. Porém, são funções anônimas que contem apenas uma linha. Ou seja, tudo deve ser contido dentro de uma unica expressão.

lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'}
]
'''
# Uso comum:
# Como argumento de funções que recebem outra função, como sorted, filter, map, reduce.

lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'}
]


def exibir_lista(lista):
    for item in lista:
        print(item)
    print()

nome = sorted(lista, key=lambda item: item['nome'])
sobrenome = sorted(lista, key=lambda item: item['sobrenome'])

exibir_lista(nome)
exibir_lista(sobrenome)

## Mais algumas funções com lambda

def executa(funcao, *args):
    return funcao(*args)

print(executa(lambda x, y: x + y, 2, 3))

##
numeros = [1, 2, 3, 4, 5, 6]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares) # Saída:

##

numeros = [2, 3, 4, 5, 6]
quadrados = list(map(lambda x: x**2, numeros))
print(quadrados) # Saída: