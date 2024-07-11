'''Como usuário quero informar um nome para saber se o nome é Pedro. 
• Critério 1 – Dados de Entrada: nome 
• Critério 2 – Condição: se o nome = “Pedro”, mostrar a Mensagem 1. 
• Critério 3 – Mensagem 1: “Olá Pedro!!! Bem-vindo de volta a nossa loja”.'''

#Entrada
nome=input("Digite um nome: ")

#Processamento e saída
if (nome=="Pedro"):
    print("Olá, Pedro!! Bem-vindo de volta a nossa loja")
else:
    print("Olá,"+nome+"!! Bem-vindo de volta a nossa loja")

