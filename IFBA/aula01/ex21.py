# 21. Crie um programa em Python que solicite ao usuário o nome, o peso e a altura de uma
# pessoa, e escreva na tela o seu IMC (Índice de Massa Corpórea).
# peso / (altura * altura)
def imc(nome, peso, altura):
    if not nome:
        print('ERRO: Digite um nome')
        return
    
    imc = peso / (altura * altura)
    if imc < 18.5:
        resultado = 'Abaixo do peso normal'
    elif 18.5 <= imc < 24.9:
        resultado = 'Peso normal'
    elif 25 <= imc < 29.9:
        resultado = 'Excesso de peso'
    elif 30 <= imc < 34.9:
        resultado = 'Obesidade classe I'
    elif 35 <= imc < 39.9:
        resultado = 'Obesidade classe II'
    else:
        resultado = 'Obesidade classe III'
    
    print(f'Seu nome é: {nome}')
    print(f'Seu IMC é: {imc:.2f}')
    print(f'{resultado}')


nome = str(input('Insira o nome: ')).strip().title()
try:
    peso = float(input('Insira o peso: '))
    altura = float(input('Insira a altura: '))
    imc(nome, peso, altura)
except ValueError:
    print('ERRO: Insira apenas números!')