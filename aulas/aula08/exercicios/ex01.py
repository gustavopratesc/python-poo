carro = {
    'marca': 'Toyota',
    'modelo': 'Corolla',
    'ano': 2022,
    'cores_disponiveis': [
        'preto', 'branco', 'azul'
    ]
}

print('-- DESCRIÇÃO DO CARRO --')
for chave, valor in carro.items():
    print(f'{chave}: {valor}')