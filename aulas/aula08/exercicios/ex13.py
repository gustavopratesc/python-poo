estoque = {
    'nome do produto': ['Celular', 'Notebook', 'Tablet'],
    'valor': [800, 2500, 1200],
    'quantidade': [8, 5, 10],
}

print(f'Número de produtos: {len(estoque["nome do produto"])}')
print(f'Apenas as chaves do dicionario: {estoque.keys()}')
print(f'Apenas os valores do dicionario: {estoque.values()}')

if estoque.get('desconto') is None:
    estoque.setdefault('desconto', 0.1)
else:
    print(f'Desconto ja existe {estoque['desconto']}')

print(estoque)


