agenda = {
    'nome': 'Gustavo',
    'telefone': 77988529963,
    'telefone3': 7798888888
}

if agenda.get('telefone2') is None:
    print('Contato não encontrado!') 

# agenda.pop('telefone')

agenda.popitem()

print(agenda)