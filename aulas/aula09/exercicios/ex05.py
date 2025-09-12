# Crie um jogo onde o usuário vai digitando letras e você armazena em um set as letras já digitadas.

# Se a letra "x" for digitada, o jogo termina.

# Se o usuário repetir uma letra, informe "Você já digitou essa letra!".

# No final mostre todas as letras digitadas.

# Crie um programa que recebe uma lista de palavras e retorna somente as palavras únicas usando set.

conjunto_de_letras = set()

def jogo_letra():
    contador = 0
    while True:
        letra = str(input('Insira uma letra: ')).strip().lower()
        if letra:
            contador += 1
            if letra in conjunto_de_letras:
                print('Você Ja digitou essa letra')
            conjunto_de_letras.add(letra)
            print(f'{conjunto_de_letras}')
        else:
            print('ERRO: Digite alguma coisa!')


        if letra == 'x':
            print('Você acertou!!')
            print(f'Tentativas {contador}')
            break

jogo_letra()