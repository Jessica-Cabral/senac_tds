'''Como usuário quero informar o valor da conta de luz para saber se estou gastando muito ou está normal.
• Critério 1 – Dados de Entrada: valor conta
• Critério 2 – Condição: se valor <= R$ 200, está normal, mostrar a Mensagem 1. Senão, está gastando muito, mostrar a Mensagem 2. 
• Critério 3 – Mensagem 1: “Normal” 
• Critério 4 – Mensagem 2: “Pare enquanto ainda consegue pagar”'''

#Entrada
valorConta=float(input("informe o valor da conta: "))

#Processamento e saída
if (valorConta<=200):
    print("Gasto normal!")
else:
    print("Pare enquanto ainda consegue pagar!")

