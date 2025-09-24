# 21. Para uma lista de caracteres (ou uma string convertida em lista), substitua todas as
# vogais por *.

lista_caracteres = ['a', 'b', 'c', 'i', 'o']


for i in range(len(lista_caracteres)):
    if lista_caracteres[i] in 'aeiouAEIOU':
        lista_caracteres[i] = '*'

print(lista_caracteres)