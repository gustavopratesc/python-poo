def media_notas(lista_nota):
    media = sum(lista_nota) / len(lista_nota)
    return f'{media:.2f}'

lista_notas = []

try:
    for i in range(3):
        nota = float(input(f'Insira a nota {i + 1}°: '))
        lista_notas.append(nota)
except ValueError:
    print('ERRO: Valor inserido não é númerico!')

print(f'A media desse aluno é: {media_notas(lista_notas)}')
