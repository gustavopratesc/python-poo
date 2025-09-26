pessoa = {
    'nome': 'Gustavo',
    'idade': 22,
    'cidade': 'Salvador',
    'curso': 'Sistemas'
}

nova_pessoa = {
    chave: (valor if isinstance(valor, (int, float)) else valor.upper()) 
    for chave, valor in pessoa.items() 
    if chave != 'curso'}


print(nova_pessoa)