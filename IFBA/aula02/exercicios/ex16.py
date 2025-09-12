# 16. Crie um programa em Python que solicite ao usuário o salário e o tempo de serviço em
# meses. Se o tempo de serviço for maior que 5 anos, conceda um bônus de 10% no seu
# salário.

def bonus(salario, tempo):
    tempo_meses = tempo / 12
    if tempo_meses > 5:
        print(f'Você esta a mais de {tempo_meses:.2f} anos na empresa')
        print(f'Você vai receber 10% a mais de dinheiro no salario')
        novo_bonus = salario + (salario * 0.10)
        print(f'Seu salario antigo R${salario} Seu novo salario R${novo_bonus}')
        return
    
    print(f'Você trabalha a {tempo_meses} aqui ainda não vai receber aumento')
    print(f'Seu salario R${salario}')


try:
    salario = float(input('Insira o seu salario: R$'))
    tempo = int(input('Insira o seu tempo em meses: '))
    bonus(salario, tempo)
except ValueError:
    print('ERRO: Insira apenas números!')