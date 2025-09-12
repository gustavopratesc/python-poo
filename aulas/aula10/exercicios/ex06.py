palavras = ['python', 'java', 'c', 'javascript', 'go', 'rust']

lista_3_palavras = filter(lambda palavra: len(palavra) > 5, palavras)

print(list(lista_3_palavras))
