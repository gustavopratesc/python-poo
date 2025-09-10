# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '2',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '0',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '1',
    },
]

for pergunta in perguntas:
    print(f"Pergunta: {pergunta['Pergunta']}")
    print("Opções:")
    for i, opcao in enumerate(pergunta['Opções']):
        print(f"[{i+1}] {opcao}")
    print("-" * 20)

for pergunta in perguntas:
    resposta_correta = pergunta['Resposta']
    resposta_usuario = input(f"Digite a sua resposta para '{pergunta['Pergunta']}': ")
    
    if resposta_usuario == resposta_correta:
        print("Você acertou!")
        acertos += 1
    else:
        print(f"Você errou. A resposta correta era '{resposta_correta}'.\n")

print(f"Fim do jogo! Você acertou {acertos} de {len(perguntas)} perguntas.")