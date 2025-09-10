

funcionarios = {
    'id1': {'nome': 'Gustavo Prates Caetano', 'cargo': 'Desenvolvedor', 'salario': 2000},
    'id2': {'nome': 'João Pedro', 'cargo': 'Arquiteto', 'salario': 1500},
    'id3': {'nome': 'Maria Elena', 'cargo': 'Engenheira Eletrica', 'salario': 1700}
}

print(f'Ids dos funcionarios: {funcionarios.keys()}')

nomes = [dados['nome'] for dados in funcionarios.values()] # list comprension
print(f'Todos os nomes: {nomes}')

## ou

for id_func, dados in funcionarios.items():
    print(f'{id_func}: {dados['nome']}')
