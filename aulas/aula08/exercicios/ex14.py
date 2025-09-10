'''AQUI A COPIA DO ALUNO2 VAI ALTERAR O ALUNO1 EM QUESTÃO DA LISTA OS DOIS VAI FICAR 400 NA POSIÇÃO 1 DE NOTAS'''
# aluno = {
#     'aluno': 'Gustavo Prates Caetano',
#     'idade': 21,
#     'notas': [20, 23, 27]
# }

# aluno2 = aluno.copy()

# aluno2['notas'][1] = 400

# print(aluno)
# print(aluno2)

'''AGORA AQUI NÃO VAI FICAR POIS IRA UTILIZAR O IMPORT COPY | DEEPCOPY'''

import copy

aluno = {
    'aluno': 'Gustavo Prates Caetano',
    'idade': 21,
    'notas': [20, 23, 27]
}

aluno2 = copy.deepcopy(aluno)

aluno2['notas'][1] = 400

print(aluno)
print(aluno2)