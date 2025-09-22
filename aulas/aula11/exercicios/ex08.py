def cadastro(id, **dados):
    print(f'-- DADOS CADASTRO --')
    print(f'Seu id: {id}')
    for k, v in dados.items():
        print(f'{k}: {v}')


try:
    id = int(input('Insira seu id: '))
    nome = str(input('Insira seu nome: ')).strip().title()
    if not nome:
        print('ERRO: Insira um nome')
    idade = int(input('Insira uma idade: '))
    dados_cadastro = {}
    dados_cadastro['nome'] = nome
    dados_cadastro['idade'] = idade
    cadastro(id, **dados_cadastro)
except ValueError:
    print('ERRO: Insira apenas números')


