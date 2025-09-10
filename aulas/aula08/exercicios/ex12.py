contatos = {
    'contato1': 77988529963,
    'contato2': 77988692493,
    'contato3': 77988041710
}

del contatos['contato3']

if contatos.get('contato3') is None:
    print(f'Contato: não encontrado')
else:
    print(f'Contato encontrado!: {contatos['contato3']}')