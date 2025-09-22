def saudar(*nomes, **comprimento):
    lista_comprimentos = list(comprimento.values())
    for i, nome in enumerate(nomes):
        cumprimento = lista_comprimentos[i % len(lista_comprimentos)]
        print(f'{cumprimento}, {nome}')

lista_nomes = []

while True:
    nome = str(input('Insira um nome: ')).strip().title()
    lista_nomes.append(nome)
    continuar = input('Quer continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break



comprimentos = {
    'comprimento1': str(input('Insira seu 1° comprimento: ')),
    'comprimento2': str(input('Insira seu 2° comprimento: ')),
    'comprimento3': str(input('Insira seu 3° comprimento: '))
}

saudar(*lista_nomes, **comprimentos)