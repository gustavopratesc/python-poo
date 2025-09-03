def saudacao(nome='Desconhecido'):
    print(f'Olá, {nome} seja Bem vindo!')

nome = str(input('Insira seu nome: ')).strip().title()
if not nome:
    print('Nenhum nome Digitado!')
saudacao(nome)