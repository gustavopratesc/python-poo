#dada uma tupla retornem o segundo maior elemento

tupla = (10, 50, 60, 67, 85, 90)

nova_tupla = sorted(tupla, reverse=True) # ordenou e reverteu e pegou o 2 indice

print(f'O segundo maior é: {nova_tupla[1]}')

