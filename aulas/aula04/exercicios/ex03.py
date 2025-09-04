def saudacao(nome):
    return f'Olá {nome}, seja bem vindo!'

nome = str(input('Insira seu nome: ')).strip().title()
if not nome:
    print('ERRO: Nenhum valor digitado!')
else:
    print(saudacao(nome))
    