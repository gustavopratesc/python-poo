def dados_pessoais(**dados):
    for chave, valor in dados.items():
        print(f'{chave}: {valor}')

dados = {

    'nome':  str(input('Insira seu nome: ')).strip().title(),
    'idade':  int(input('Insira sua idade: ')),
    'cidade': str(input('Insira a sua cidade: ')).strip().title()

}

dados_pessoais(**dados)