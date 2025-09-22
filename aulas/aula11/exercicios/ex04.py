# Crie uma função cadastro que aceita:

# um ID obrigatório,

# dados adicionais ilimitados com **kwargs.

def cadastro(id, **dados_adicionais):
    print('-- CADASTRO --')
    print(f'Seu id: {id}')
    print(f'Seus dados: ')
    for k, v in dados_adicionais.items():
        print(f'{k}: {v}')


try:
    id = int(input('Insira um id: '))
    nome = str(input('Insira um nome: ')).strip().title()
    cidade = str(input('Insira uma cidade: ')).strip().title()
    cep = int(input('Insira o seu CEP só números: '))
    cpf = int(input('Insira o seu CPF só números: '))
    cadastro(id, nome=nome, cidade=cidade, cep=cep, cpf=cpf)
except ValueError:
    print('ERRO: Insira apenas números!')