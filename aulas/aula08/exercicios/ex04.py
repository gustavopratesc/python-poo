livro = {
    'titulo': 'Python para Iniciantes',
    'autor': 'Jose da Silva',
    'ano': 2023,
    'capitulos': ['Introdução', 'Variaveis', 'Estrutura de Dados'],
    'profissao': 'programador' 
}

print(f'Nome do segundo capitulo: {livro["capitulos"][1]}')
for chave, valor in livro.items():
    print(f'{chave}: {valor}')