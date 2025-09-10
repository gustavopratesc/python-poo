"""EXERCICIOS
CRIE FUNÇÕES QUE DUPLICAM, TRIPLICAM, E QUADRUPLICAM
O NÚMERO RECEBIDO COMO PARAMETRO
"""

# def duplicar(numero):
#     return numero * 2

# def triplicar(numero):
#     return numero * 3

# def quadruplicar(numero):
#     return numero * 4


# def tudo_junto(numero):
#     duplicar = numero * 2
#     triplicar = numero * 3
#     quadruplicar = numero * 4
#     print(f'Duplicado: {duplicar} | Triplicado {triplicar} | Quadruplicado {quadruplicar}')

# print(duplicar(2))
# print(triplicar(3))
# print(quadruplicar(4))
# tudo_junto(10)


def multiplicar(multiplicador):
    def multi(numero):
        return numero * multiplicador
    return multi


duplicar = multiplicar(2)
triplicar = multiplicar(3)
quadruplicar = multiplicar(4)

print(duplicar(10))
print(triplicar(10))
print(quadruplicar(10))