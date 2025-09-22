# 35. Crie um programa em Python que leia a idade e peso de um paciente e escreva a
# dosagem que ele deve tomar de um medicamento, em gotas. Pessoas com 12 anos ou
# mais, e com peso igual ou superior a 60 kg devem tomar 40 gotas, mas com 12 anos ou
# mais, e peso abaixo de 60 kg devem tomar 30 gotas. Crianças abaixo de 12 anos a
# dosagem é calculada pelo peso corpóreo, sendo a dosagem de 1 gota a cada 2 kg de peso.


def dosagem(idade, peso):
    if idade < 12:
        dosagem_medicamento = peso / 2
        return f'O paciente é uma criança e deve tomar {dosagem_medicamento:.0f} gotas'
    elif idade >= 12 and peso >= 60:
        return f'O paciente deve tomar 40 gotas do remedio'
    elif idade >= 12 and peso < 60:
        return f'O paciente deve tomar 30 gotas do remedio'


try:
    idade = int(input('Insira sua idade: '))
    peso = float(input('Insira seu peso: '))
    resultado = dosagem(idade, peso)
    print(resultado)
except ValueError:
    print('ERRO: Insira apenas números inteiros!')