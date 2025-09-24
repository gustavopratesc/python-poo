# 17. Verifique se duas listas são iguais (mesmos elementos na mesma ordem)

lista1 = ['Gustavo', 'Maria', 'Jose']
lista2 = ['Maria', 'Jose', 'Gustavo']

new_lista1 = sorted(lista1)
new_lista2 = sorted(lista2)

if new_lista1 == new_lista2:
    print('São iguais')
else:
    print('Não')