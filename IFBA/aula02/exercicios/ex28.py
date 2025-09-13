# 28. Crie um programa em Python que leia a sigla de um estado e o nome de uma pessoa e
# informe se ela é carioca, paulista, mineira, ou é de outro estado.

sigla = str(input('Insira a sua sigla do seu estado: ')).strip().upper()
if not sigla.isalpha():
    print('ERRO: Digite apenas letras!')
else:
    if sigla == 'RJ':
        print('Você é carioca')
    elif sigla == 'SP':
        print('Você é paulista')
    elif sigla == 'MG':
        print('Você é de mineiro')
    else:
        print('Você é de outro estado!')