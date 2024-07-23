'''Como usuário quero informar minha idade para saber posso me aposentar. 
• Critério 1 – Dados de Entrada: idade 
• Critério 2 – Condição: se idade>=100, mostrar a Mensagem 1. 
• Critério 3 – Mensagem 1: “Se estiver vivo pode se aposentar.”'''

#Entrada
idade=int(input("informe sua idade: "))


#Processamento e saída
if (idade>=100):
    print("Se estiver vivo pode se aposentar")
else:
    print("Idade não permite aposentadoria!")

