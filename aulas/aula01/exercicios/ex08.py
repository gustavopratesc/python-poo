def saudacao(nome="Visitante", horario=0):
    if 0 <= horario <= 12:
        print(f'Bom dia, {nome}!')
    elif 12 < horario <= 18:
        print(f'Boa tarde, {nome}!')
    else:
        print(f'Boa noite, {nome}!')


nome = input('Insira seu nome: ').strip().title()

if not nome:
    nome = "Visitante"

try:
    horario = float(input('Insira o horario: '))
    saudacao(nome, horario)
except ValueError:
    print(f'ERRO: Digite um número!')
