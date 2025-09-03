# cada pasta de aula vai ter seus exercicios
# defs

""" Introdução às funções (def) em Python funções são trechos de codigo usados para replicar determinada ação ao longo do seu codigo. Elas podem receber valores para parâmetros (argumentos) e retornar um valor especifico. Por padrão, funções Python retornam None (Nada) """

def imprimir(a, b, c): # a, b, c são os parametros
    s = a + b + c
    return s

a = 12
b = 15
c = 14

print(imprimir(a, b, c)) # a, b, c são argumentos

def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}')

saudacao('Gustavo')