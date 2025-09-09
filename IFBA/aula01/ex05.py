# 5. Crie um programa em Python que solicite ao usuário 2 valores, em seguida, troque o
# valor dessas variáveis e imprima os novos valores.

def troca_valor(valor1, valor2):
    valor1 = 'Resposta trocada'
    valor2 = 'kkkkk'
    return f'{valor1} {valor2}'


valor1 = input('Insira alguma coisa: ')
valor2 = input('Insira outra coisa: ')

print(f'{troca_valor(valor1, valor2)}')