def concatenar_strings(palavra):
    juntar_palavras = " ".join(palavra)
    return juntar_palavras
lista_palavras = []

while True:
    print('Digite uma palavra ou enter para finalizar!')
    palavra = input('Insira a palavra: ')
    lista_palavras.append(palavra)
    if not palavra:
        print(f'As palavras juntas: {concatenar_strings(lista_palavras)}')
        break
