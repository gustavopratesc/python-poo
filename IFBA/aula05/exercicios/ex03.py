tupla = (1, 2, 3, 4, 6) # pegou uma tupla

lista_tupla = list(tupla) # transformou em lista

lista_tupla[4] = 5 # modificou através da lista

tupla_lista = tuple(lista_tupla) # transformou a lista em tupla

print(tupla_lista)