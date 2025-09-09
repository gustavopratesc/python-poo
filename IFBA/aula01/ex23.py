# 23. Crie um programa em Python que declare uma variável do tipo string e a inicialize com o
# nome de uma pessoa em minúsculo. Converta esse texto para maiúsculo e imprima o
# resultado

def maiusculo(nome):
    nome_maiusculo = nome.upper()
    return nome_maiusculo


nome = str(input('Insira seu nome: ')).strip().lower()
if not nome:
    print('ERRO: Insira um nome!')
else:
    print(f'Seu nome em maiusculo: {maiusculo(nome)}')