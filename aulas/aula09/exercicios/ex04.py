
conjuntos_texto = set()

while True:
    texto = input('Digite alguma coisa ou Enter para finalizar: ')
    if texto:
        conjuntos_texto.add(texto)
        print(conjuntos_texto)
    else:
        print('Você resolveu finalizar o programa')
        break

print(f'{conjuntos_texto}')