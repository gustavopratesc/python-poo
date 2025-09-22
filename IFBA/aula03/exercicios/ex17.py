# 17. Crie um programa em Python que leia nome, idade e sexo de 20 pessoas. Imprimir o
# nome todo em maiúsculo se a pessoa for do sexo masculino e tiver mais de 21 anos


def nome_maiusculo(lista_usuarios):
    for i, v in enumerate(lista_usuarios):
        if v[1] > 21 and v[2] in ['masculino', 'm', 'homem']:
            print(f'O seu nome em {i + 1} maiusculo: {v[0].upper()}')
            

lista_usuarios = []

for i in range(1, 21):
    while True:
        nome = input(f'Insira o {i}° nome: ').strip().title()
        if not nome:
            print('ERRO: Insira apenas o nome!')
        else:
            break
    while True:
        try:
            idade = int(input(f'Insira a {i}° idade: '))
            break
        except ValueError:
            print('ERRO: Insira apenas números para idade!')
            
    while True:
        sexo = input(f'Insira o {i}° sexo: ').strip().lower()
        if not sexo:
            print('ERRO: Insira apenas o sexo!')
        else:
            break
    print('-------')
    lista_usuarios.append((nome, idade, sexo))
            
nome_maiusculo(lista_usuarios)

## ou

def nome_maiusculo(lista_usuarios):
    for i, v in enumerate(lista_usuarios):
        nome, idade, sexo = v  # desempacotar tupla
        if idade > 21 and sexo in ['masculino', 'm', 'homem']:
            print(f'{i+1}ª pessoa (nome em maiúsculo): {nome.upper()}')

lista_usuarios = []

for i in range(1, 21):
    
    while True:
        nome = input(f'Insira o {i}° nome: ').strip().title()
        if not nome:
            print('ERRO: Insira apenas o nome!')
        else:
            break


    while True:
        try:
            idade = int(input(f'Insira a {i}° idade: '))
            break
        except ValueError:
            print('ERRO: Insira apenas números para idade!')

    
    while True:
        sexo = input(f'Insira o {i}° sexo: ').strip().lower()
        if not sexo:
            print('ERRO: Insira apenas o sexo!')
        else:
            break

    print('-------')
    lista_usuarios.append((nome, idade, sexo))

nome_maiusculo(lista_usuarios)
