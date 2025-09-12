'''14. Crie um programa em Python que solicite ao usuário o peso de um produto. Se o peso
for maior que 10 kg, calcule o frete com 20% de acréscimo; caso contrário, aplique frete
normal.'''

frete = 15

def frete_produto(peso_produto):
    if peso_produto > 10:
        print('Você esta com um produto com +10Kg você vai pagar 20% acrescimo frete')
        novo_frete = frete + (frete * 0.2)
        print(f'O frete antigo era R${frete} o novo frete agora é R${novo_frete:.2f}')
        return
    
    print(f'Você ira pagar apenas R${frete} de frete')

try:
    peso_produto = float(input('Insira o peso do produto em KG: '))
    frete_produto(peso_produto)
except ValueError:
    print('ERRO: Insira apenas valores númericos!')
