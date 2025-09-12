# 7. Crie um programa em Python que solicite ao usuário um valor de investimento. Se o valor
# for maior que R$10.000,00, imprima "Investimento Alto", senão, imprima "Investimento
# Baixo".

def valor_investimento(valor):
    if valor > 10000:
        print('Investimento alto!')
    else:
        print('Investimento baixo!')


try:
    valor = float(input('Insira o valor do investimento: R$'))
    valor_investimento(valor)
except ValueError:
    print('ERRO: Insira apenas números númericos!')