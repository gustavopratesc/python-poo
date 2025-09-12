pessoas = [
    {'nome': 'João', 'idade': 25},
    {'nome': 'Ana', 'idade': 30},
    {'nome': 'Pedro', 'idade': 20},
    {'nome': 'Carla', 'idade': 35}
]

idade_ordenada = sorted(pessoas, key=lambda idade: idade['idade'])

for i in idade_ordenada:
    print(i['idade'])