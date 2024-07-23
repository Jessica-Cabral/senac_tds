'''Como usuário quero informar dois números para saber se o primeiro é menor que o segundo número.
• Critério 1 – Dados de Entrada: primeiro, segundo 
• Critério 2 – Condição: se o primeiro < segundo, mostrar a Mensagem 1. 
• Critério 3 – Mensagem 1: “O primeiro número é menor que o segundo número.”'''

#Entrada
primeiro=float(input("Digite o primeiro número: "))
segundo=float(input("Digite o segundo número: "))

#Processamento e saída
if (primeiro<segundo):
    print("O primeiro número é menor que o segundo número.")
else:
    print("O primeiro número não é menor que o segundo número.")

