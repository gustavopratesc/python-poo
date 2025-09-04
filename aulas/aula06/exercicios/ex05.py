def dobro(x):
    return x * 2

def triplo(x):
    return x * 3

def quadrado(x):
    return pow(x, 2)

lista_funcoes = [
    dobro,
    triplo,
    quadrado
]

def executa(lista_funcoes, valor):
    resultados = []
    for funcao in lista_funcoes:
        resultados.append(funcao(valor))
    return resultados
    

print(executa(lista_funcoes, 4))