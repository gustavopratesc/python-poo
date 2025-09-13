'''19. Crie um programa em Python que leia os nomes e os tempos de 3 atletas de atletismo
numa corrida de 100 m, e informe quem é o campeão, quem é o vice-campeão e quem
ficou com o terceiro lugar. Considere que os tempos são sempre diferentes e que quem tem
o melhor desempenho é quem tem o menor tempo.'''

print('-- CORRIDA DE 100M --')
nome1 = str(input('Insira o primeiro nome: ')).strip().title()
nome2 = str(input('Insira o segundo nome: ')).strip().title()
nome3 = str(input('Insira o terceiro nome: ')).strip().title()

try:
    tempo1 = float(input(f'Insira o tempo do {nome1}: '))
    tempo2 = float(input(f'Insira o tempo do {nome2}: '))
    tempo3 = float(input(f'Insira o tempo do {nome3}: '))
except ValueError:
    print('ERRO: Insira apenas números!')

if tempo1 < tempo2 and tempo1 < tempo3:
    print(f'O {nome1} foi campeão!')
    if tempo2 < tempo3:
        print(f'O {nome2} foi vice-campeão!')
        print(f'O {nome3} ficou em terceiro lugar!')
    else:
        print(f'O {nome3} foi vice-campeão!')
        print(f'O {nome2} ficou em terceiro lugar!')
elif tempo2 < tempo1 and tempo2 < tempo3:
    print(f'O {nome2} foi campeão!')
    if tempo1 < tempo3:
        print(f'O {nome1} foi vice-campeão')
        print(f'O {nome3} ficou em terceiro lugar!')
    else:
        print(f'O {nome3} foi vice campeão')
        print(f'O {nome1} ficou em terceiro lugar!')
else:
    print(f'O {nome3} foi campeão!')
    if tempo1 < tempo2:
        print(f'O {nome1} foi vice-campeão')
        print(f'O {nome2} ficou em terceiro lugar!')
    else:
        print(f'O {nome2} foi vice-campeão')
        print(f'O {nome1} ficou em terceiro lugar!')

### outra forma
print('-- CORRIDA 100M --')
atletas = []

for i in range(3):
    nome = input(f'Insira o nome do {i + 1}° atleta: ').strip().title()
    tempo = float(input(f'Insira o tempo do {i + 1}° atleta: '))
    atletas.append((nome, tempo))

atletas_ordenados = sorted(atletas, key=lambda x: x[1])

print('-- RESULTADOS --')
for i, (nome, tempo) in enumerate(atletas_ordenados, start=1):
    if i == 1:
        print(f'{nome} foi campeão! com tempo {tempo}')
    elif i == 2:
        print(f'{nome} foi vice-campeão! com tempo {tempo}')
    else:
        print(f'{nome} ficou em terceiro lugar com tempo {tempo}')

