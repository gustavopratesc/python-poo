# 31. Crie um programa em Python que solicite o nome e a idade de um usuário e escreva na
# tela se ele é Criança(entre 0 e 12 anos), Adolescente (entre 13 e 18 anos), Adulto (entre 18
# e 60 anos) ou Idoso (igual ou superior a 60 anos).

def crescimento(nome, idade):
    if 0 < idade <= 12:
        print(f'Seu nome é {nome} | Possui {idade} anos | É criança')
    elif 13 < idade < 18:
        print(f'Seu nome é {nome} | Possui {idade} anos | É adolescente')
    elif 18 <= idade <= 60:
        print(f'Seu nome é {nome} | Possui {idade} anos | É adulto')
    else:
        print(f'Seu nome é {nome} | Possui {idade} anos | É idoso')


nome = str(input('Insira seu nome: ')).strip().title()
if not nome.isalpha():
    print('ERRO: Insira apenas o nome!')
else:
    try:
        idade = int(input('Insira sua idade: '))
        crescimento(nome, idade)
    except ValueError:
        print('ERRO: Digite apenas números inteiros!')