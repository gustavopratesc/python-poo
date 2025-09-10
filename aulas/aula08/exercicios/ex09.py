produto = {
    'nome': 'Camiseta',
    'preço': 39.90 
}

produto['estoque'] = 100

for k, v in produto.items(): # k = key, v = value
    print(f'{k}: {v}')

del produto['estoque']

print(produto)