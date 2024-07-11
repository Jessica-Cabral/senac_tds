'''Como usuário quero informar um número inteiro para saber se o número é zero.
• Critério 1 – Dados de Entrada: número 
• Critério 2 – Condição: se o número = 0, mostrar a Mensagem 1. 
• Critério 3 – Mensagem 1: “O número digitado é 0”'''

#Entrada
numero=int(input("Digite um número: "))

#Processamento e saída
if (numero==0):
    print("O número é zero")
else:
    print("O número não é zero")

