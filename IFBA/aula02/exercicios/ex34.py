# 34. Crie um programa em Python que leia o salário mensal de uma pessoa e escreva qual o
# valor que ela deve devolver ao Governo Federal no Imposto de Renda de Pessoa Física
# (IRPF). A seguir a tabela com as alíquotas por faixa salarial. Salário até 1903,98 é Isento;
# De 1903,99 a 2826,65 sofre alíquota de 7,5%; De 2826,66 a 3751,05 sofre alíquota de
# 15,0%; De 3751,06 a 4464,68 sofre alíquota de 22,5%; e Acima de 4464,68 sofre alíquota
# de 27,5%.

def imposto_governo(salario):
    if salario <= 1903.98:
        return 'Você é Isento do IRPF'
    elif 1903.99 <= salario <= 2926.65:
        aliquota = salario * 0.075
        return f'Você paga R${aliquota:.2f} ao governo'
    elif 2826.66 <= salario <= 3751.05:
        aliquota = salario * 0.15
        return f'Você paga R${aliquota:.2f} ao governo'
    elif 3751.06 <= salario <= 4464.68:
        aliquota = salario * 0.225
        return f'Você paga R${aliquota:.2f} ao governo'
    else:
        aliquota = salario * 0.275
        return f'Você paga R${aliquota:.2f} ao governo'

print('CALCULADORA DE IMPOSTO')
try:
    salario = float(input('Insira o seu salario: R$'))
    resultado = imposto_governo(salario)
    print(resultado)
except ValueError:
    print('ERRO: DIGITE APENAS NÚMEROS')