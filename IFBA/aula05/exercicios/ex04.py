#dada uma tupla de tuplas por exemplo ((1,2), (3,4), (5,6)) crie uma lista com a soma de cada tupla interna (ex: [3, 7, 11])

tupla = ((1, 2), (3, 4), (5, 6))

lista = []
for i, v in enumerate(tupla):
    soma = sum(v)
    lista.append(soma)
    

print(lista)