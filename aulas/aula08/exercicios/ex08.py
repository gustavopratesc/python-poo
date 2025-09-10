aluno = {
    'nome': 'Gustavo',
    'idade': 21
}

aluno['curso'] = 'Sistemas de Informação'

for chave, valor in aluno.items():
    print(f'{chave}: {valor}')