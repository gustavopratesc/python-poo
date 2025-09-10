carro = {
    'marca': 'Toyota',
    'modelo': 'Corolla',
    
}

# carro['ano'] = 2020

if carro.get('ano') is None:
    print('Ano não informado')
else:
    print(carro['ano'])