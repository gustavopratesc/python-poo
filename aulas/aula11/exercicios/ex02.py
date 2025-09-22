def mostrar_info(*args, **kwargs):
    print('-- HOBBIES --')
    for h in args:
        print(h)
    
    print('-- DADOS PESSOAIS --')
    for c, v in kwargs.items():
        print(f'{c}: {v}')


lista_hobbies = []

while True:
    hobbies = str(input('Insira seu hobbie: ')).strip().title()
    lista_hobbies.append(hobbies)
    continuar = input('Quer continuar? [S/N]: ').strip().upper()
    if continuar == 'S':
        continue
    else:
        break

dados_pessoais = {
    'nome': str(input('Insira seu nome completo: ')).strip().title(),
    'idade': int(input('Insira a sua idade: ')),
    'cidade': str(input('Insira a sua cidade: ')),
    'cpf': input('Insira seu CPF: ')
}

mostrar_info(*lista_hobbies, **dados_pessoais)
