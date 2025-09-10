
def merge_dicts(d1, d2):
    newdict = {}
    newdict.update(d1)
    newdict.update(d2)
    return newdict

# ## ou kwargs
# def merge_dicts(d1, d2):
#     return {**d1, **d2}  # junta os dois dicionários em um novo

dict1 = {
    'nome': 'Gustavo',
    'idade': 21
}

dict2 = {
    'email': 'gustavoprates.c@hotmail.com',
    'cidade': 'Vitoria da Conquista'
}

print(merge_dicts(dict1, dict2))