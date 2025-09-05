def criar_logger(prefixo):
    def mensagem(msg):
        return f'{prefixo} {msg}'
    return mensagem

erro = criar_logger("[ERRO]")
info = criar_logger("[INFO]")

print(erro("Arquivo não encontrado"))
print(info("Processo iniciado"))

#  ou

def criar_logger(prefixo):
    def mensagem(msg):
        print(f'{prefixo} {msg}')
    return mensagem

erro = criar_logger("[ERRO]")
info = criar_logger("[INFO]")

erro("Arquivo não encontrado")
info("Processo iniciado")
