'''Como usuário quero informar a idade para saber se estou apto a tirar carteira de motorista.
• Critério 1 – Dados de Entrada: idade
• Critério 2 – Condição: se idade>18 anos, está apto, mostrar a Mensagem 1. Senão, é menor de idade, mostrar a Mensagem 2. 
• Critério 3 – Mensagem 1: “Apto” 
• Critério 4 – Mensagem 2: “Menor de idade.”'''

#Entrada
idade=float(input("informe a idade: "))

#Processamento e saída
if (idade>=18):
    print("Apto!")
else:
    print("Menor de idade!")

