def configurar_app(**opcoes):
    print('Suas configurações')
    for k, v in opcoes.items():
        print(f'{k}: {v}')



opcoes = {
    'tema': str(input('Qual tema você quer? Claro ou Escuro: ')).strip().title(),
    'idioma': str(input('Idioma que deseja: ')).strip().title(),
    'notificacoes': str(input('Notificações Sim ou Não?: '))
}

configurar_app(**opcoes)