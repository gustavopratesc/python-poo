"""
Argumentos nomeados e não nomedos em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apeas o argumento (valor posicional)
"""

def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z =', x + y + z)


soma(1, 2, 3) # <-- argumentos posicionais
soma(x=1, y=2, z=5) # argumentos nomeados