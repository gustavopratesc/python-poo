nomes = ['Maria', 'José', 'Paulo']
sobrenomes = ['Silva', 'Souza', 'Oliveira']

nome_completo = map(lambda nome, sobrenome: f'{nome} {sobrenome}', nomes, sobrenomes)

print(list(nome_completo))