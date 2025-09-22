def criar_usuario(**dados):
    print('Seus dados: ')
    for k, v in dados.items():
        print(f'{k}: {v}')


dados = {
    'nome': str(input('Nome: ')).strip().title(),
    'idade': int(input('Idade: ')),
    'profissão': str(input('Profissão: ')).strip().title(),
    'cidade': str(input('Cidade: ')).strip().title(),
    'cpf': int(input('CPF: '))
}

criar_usuario(**dados)