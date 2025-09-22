def mensagem_carta(**dados):
    for k, v in dados.items():
        print(f'{k}: {v}')

remetente = str(input('Insira o remetente: '))
destinatario = str(input('Insira o destinatario: '))
t_mensagem = str(input('Insira a mensagem: '))

mensagem_carta(de=remetente, para=destinatario, mensagem=t_mensagem)