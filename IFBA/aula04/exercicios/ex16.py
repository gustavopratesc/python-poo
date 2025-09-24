# 16. Dada uma lista, encontre e imprima o índice da primeira ocorrência de um elemento
# específico; se ele não existir, imprima -1.

lista = ['João', 'Gustavo', 'Jose', 'Maria']

nome = str(input('Digite algum nome: ')).strip().title()

print(lista.index(nome) if nome in lista else -1)