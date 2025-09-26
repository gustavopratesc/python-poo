produtos = [
    {'nome': 'caderno', 'preço': 15},
    {'nome': 'caneta', 'preço': 3},
    {'nome': 'mochila', 'preço': 120},
]

novo_produto = [
    {**produto, 'preço': produto['preço'] + (produto['preço'] * 0.08) if produto['preço'] > 10 else {**produto}}  
    for produto in produtos]
# ou

novo_produto = [
    (
        {**produto, 'preço': produto['preço'] * 1.08}  # aumenta 8%
        if produto['preço'] > 10 else produto         # se <= 10, mantém igual
    )
    for produto in produtos
]
print(novo_produto)