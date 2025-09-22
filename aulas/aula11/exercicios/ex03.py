
d1 = {'nome': 'Aline'}
d2 = {'idade': 20}
d3 = {'cidade': 'Salvador'}

tudo_junto = {
    **d1,
    **d2,
    **d3
}

print(tudo_junto)

