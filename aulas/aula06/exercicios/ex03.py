def maiusculo(palavra):
    return palavra.upper()


def executa(funcao, *args):
    return funcao(*args)
    

print(executa(maiusculo, 'gustavo')) # executa no 1° argumento pega a função maiusculo, no 2° argumento ela pega o geral que é o *args que no caso é gustavo e transforma em maiuscula