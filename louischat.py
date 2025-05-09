import time

def saudacao():
    print("----- Bem-vindo ao LouisChat -----")
    print("Aqui você pode conversar através do terminal\n")
    nome = input("Para começar, digite seu nome: ").strip().title()
    print(f"\nOlá, {nome}! 😄")
    return nome

def escolher_assunto(nome):
    assunto = input(f"\nSobre o que você gostaria de conversar, {nome}? ").strip()
    print("\n---- Compilando ----")
    time.sleep(1)
    print(f"\nCerto, {assunto} é uma ótima opção! 😊")
    print(f"\nVamos lá então!\n{assunto} é realmente um assunto muito interessante.")
    print(f"A importância de {assunto} é de suma grandeza no cenário que vivemos atualmente.\n")
    return assunto

def explorar_assunto(assunto):
    input(f"O que você acha mais interessante sobre {assunto}? \n")
    resposta = input("O que você acha que agrega crescimento a isso? \n")
    resposta2 = input("O que faria de diferente? \n")
    return resposta, resposta2

def reflexao_final(resposta, resposta2, nome, assunto):
    print(f"\nSensacional sua visão, {nome}!")
    print(f"De fato, {resposta} e {resposta2} tornam o contexto de {assunto} algo mais interessante e bem trabalhado.")
    input("\nVocê acredita que suas sugestões podem se tornar soluções e ferramentas para gerar uma realidade melhor no mundo? \n")
    print(f"\nMuito legal da sua parte!\nObrigado pela conversa, {nome}, e por compartilhar sua visão comigo! 😊")
    print(f"Ate breve, {nome}!\n")

# Executando o chatbot
def iniciar_chat():
    nome = saudacao()
    assunto = escolher_assunto(nome)
    resposta, resposta2 = explorar_assunto(assunto)
    reflexao_final(resposta, resposta2, nome, assunto)

# Chamada principal
if __name__ == "__main__":
    iniciar_chat()

