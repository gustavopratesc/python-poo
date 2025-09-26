lista = [x for x in range(1, 21)]

nova_lista = [x * 2 for x in lista if x % 2 != 0]

print(f'Apenas números impares duplicados: {nova_lista}')