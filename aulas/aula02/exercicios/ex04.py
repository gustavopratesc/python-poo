def mensagem(texto, estilo, caixa):
    if caixa == 'upper':
        print(f'{estilo * 3} {texto.upper()} {estilo * 3}')
    else:
        print(f'{estilo * 3} {texto.lower()} {estilo * 3}')


mensagem("python", estilo="-", caixa="lower")
        