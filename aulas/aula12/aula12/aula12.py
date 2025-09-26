# list comprehension

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nova_lista = [x * 2 for x in lista] # <- vai multiplicar todos os elementos da lista por 2
print(nova_lista)

nova_lista = [
    numero * 2
    for numero in range(10)
]

print(nova_lista)

# mapeamento de dados com list comprehension

produtos = [
    {'nome': 'p1', 'preço': 20},
    {'nome': 'p2', 'preço': 10},
    {'nome': 'p3', 'preço': 30},
]

novos_produtos = [
    {**produto, 'preço': produto['preço'] * 1.05}
    if produto['preço'] > 20 else {**produto}
    for produto in produtos
]

print(*novos_produtos)



lista_filtrada = [n for n in range(10) if n < 5] # <- vai filtrar todos os elementos da lista que forem menores que 5


lista_tupla = [
    (x, y) for x in range(3) for y in range(3)
]

print(*lista_tupla)