'''Crie um dicionário que armazene informações de um aluno, contendo as chaves "nome", "idade" e "nota". Em seguida, imprima cada valor associado às respectivas chaves.'''

aluno = {
    'nome': 'Gustavo',
    'idade': 21,
    'nota': [7.6, 9, 10]
}

for chave, valor in aluno.items():
    print(f'{chave}: {valor}')


