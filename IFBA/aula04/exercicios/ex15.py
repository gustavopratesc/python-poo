# 15. Preencha uma lista com N números aleatórios (use random.randint), e depois ordene
# esta lista em ordem decrescente

from random import randint

lista_numeros = []

for i in range(1, 11):
    i = randint(1, 1000)
    lista_numeros.append(i)

ordem_decrescente = sorted(lista_numeros, reverse=True)
ordem_crescente = sorted(lista_numeros)


print('Ordem decrescente')
print(ordem_decrescente)
print()
print('Ordem crescente')
print(ordem_crescente)