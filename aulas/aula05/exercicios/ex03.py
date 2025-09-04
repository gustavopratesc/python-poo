def junta_frase(*frase):
    palavras_juntas = " ".join(frase)
    print(f'A frase ficou: {palavras_juntas}')

lista_palavras = []

while True:
    palavra = input('Insira uma palavra: ').strip()
    if not palavra:
        junta_frase(*lista_palavras)
        break
    lista_palavras.append(palavra)