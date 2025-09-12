# 12. Crie um programa em Python que solicite ao usuário um mês e um ano e imprima se o
# mês indicado tem 28, 29, 30 ou 31 dias.

def calendario(mes, ano):
    if 0 < mes > 12:
        print('ERRO: Digite um mês valido!')
        return

    ano_bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
    print('A maioria dos meses possui 30 dias!')
    print('Os meses 4, 6, 9 possui 31 dias')
    if ano_bissexto:
        if mes == 2:
            print('Esse mês possui 29 dias ja que o ano é bissexto!')
    else:
        print(f'Esse mês {2} possui 28 dias!')


try:
    mes = int(input('Insira o mês em número: '))
    ano = int(input('Insira o ano: '))
    calendario(mes, ano)
except ValueError:
    print('ERRO: Insira apenas números!')