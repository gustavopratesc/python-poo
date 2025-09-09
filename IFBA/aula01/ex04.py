# 4. Crie um programa em Python que lê o nome de um aluno, as notas de suas três provas e
# calcule e exiba na tela a média harmônica das provas.

def media_hamornica(nota1, nota2, nota3):
    media = 3 / ((1/nota1) + (1/nota2) + (1/nota3))
    print(f'A media harmonica das 3 notas é: {media:.2f}')


nome = str(input('Insira o nome do aluno: ')).strip().title()
if not nome.isalpha():
    print(f'ERRO: Insira o nome do aluno!')
else:
    print(f'Aluno: {nome}')
    try:
        nota1 = float(input('Insira a 1° nota: '))
        nota2 = float(input('Insira a 2° nota: '))
        nota3 = float(input('Insira a 3° nota: '))
        media_hamornica(nota1, nota2, nota3)
    except ValueError:
        print('ERRO: Digite apenas números!')