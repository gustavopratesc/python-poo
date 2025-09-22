# 33. Crie um programa em Python que leia duas notas inteiras (entre 0 e 100) de um aluno e
# informe que ele foi "Aprovado" se a média aritmética dessas notas for maior ou igual a 70;
# ou que foi "Reprovado" se esta média for menor que 30. Caso ele tenha tirado uma nota
# entre 30 e 70 é necessário ler mais uma nota referente a prova final. Ao realizar a média
# ponderada entre a nota da final e média aritmética anterior, com pesos 1/3 e 2/3
# respectivamente, informar que o aluno foi "Aprovado por Final" caso o valor obtido seja
# maior ou igual a 50; ou "Reprovado" caso seja menor que isso.

def situacao_aluno(lista_notas):
    media = sum(lista_notas) / len(lista_notas)
    if media >= 7:
        return 'Aprovado'
    elif media < 30:
        return 'Reprovado'
    else:
        prova_final = float(input('Insira a nota da prova final!'))
        nova_media = (2/3) * media + (1/3) * prova_final
        if nova_media >= 50:
            return 'Aprovado na prova final!!'
        else:
            return 'Reprovado na prova final!'


lista_notas = []

try:
    for i in range(2):
        nota = float(input(f'Insira a {i + 1}° nota: '))
        lista_notas.append(nota)

    resultado = situacao_aluno(lista_notas)
    print(resultado)
except ValueError:
    print('ERRO: Insira apenas números')