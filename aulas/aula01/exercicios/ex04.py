def media_de_notas(notas):
    media = sum(notas) / len(notas)
    print(f'A media de notas do aluno é {media:.2f}')
    if media >= 7:
        print('Aprovado!!')
    else:
        print('Reprovado!!')

lista_notas = []

try:
    for i in range(3):
        nota = int(input(f'Insira a {i + 1}° nota: '))
        lista_notas.append(nota)
    media_de_notas(lista_notas)
except ValueError:
    print('ERRO: Valor inserido não é númerico')