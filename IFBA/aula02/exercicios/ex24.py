# 24. Crie um programa em Python que lê a capital do Brasil e indique se a resposta
# informada está correta ou errada.

capital = str(input('Insira a capital do Brasil: ')).strip().title()
if capital == 'Brasilia':
    print('Resposta Correta!')
else:
    print('Você errou!!')