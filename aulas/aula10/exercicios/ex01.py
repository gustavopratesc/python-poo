produtos = [
    {'produto': 'Notebook', 'preco': 3500},
    {'produto': 'Mouse', 'preco': 50},
    {'produto': 'Teclado', 'preco': 120},
    {'produto': 'Monitor', 'preco': 900},
]

nome = sorted(produtos, key=lambda nome: nome['produto'])

for i in nome:
    print(i['produto'])


# preco = sorted(produtos, reverse=True, key=lambda preco: preco['preco'])
preco = sorted(produtos, reverse=False, key=lambda preco: preco['preco'])

for i in preco:
    print(i['preco'])