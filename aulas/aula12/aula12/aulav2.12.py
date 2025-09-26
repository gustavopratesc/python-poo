# dictionary comprehension e Set comprehension

produto = {
    'nome': 'Caneta',
    'preco': 14.99,
    'categoria': 'Papelaria'
}

dicionario_comprehension = {chave: valor if isinstance(valor, (int, float)) else valor.upper() for chave, valor in produto.items() if chave != 'categoria'}
 # isinstance(valor, (int, float)) verifica se o valor é um número inteiro ou um número de ponto flutuante se não for retorna o valor em maiúsculo mas se for retorna o valor normal
print(dicionario_comprehension)


# exemplo usando set

s1 = {i for i in range(11) if i % 2 == 0} # pega os pares

print(s1)