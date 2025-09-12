# 5. Crie um programa em Python que solicite ao usuário um ano e imprima se é bissexto ou
# não.
def ano_bissexto(ano):
    ano_bi = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
    if ano_bi:
        print('É bissexto!!')
    else:
        print('Não é!') 


try:
    ano = int(input('Insira algum ano: '))
    ano_bissexto(ano)
except ValueError:
    print('ERRO: Insira apenas números!')