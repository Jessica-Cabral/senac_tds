'''Como usuário quero informar minha idade para saber posso me aposentar. 
• Critério 1 – Dados de Entrada: idade
• Critério 2 – Condição: se idade<=17 anos, mostrar a mensagem 1. Se idade entre 18 e 65 anos, mostrar mensagem 2. Se idade>65, mostrar mensagem 3 
• Critério 3 – Mensagem 1: “Muito jovem para se aposentar.” 
• Critério 4 – Mensagem 2: “Tem que trabalhar muito ainda!” 
• Critério 5 – Mensagem 3: “Se estiver vivo pode se aposentar.”'''

#Entrada
idade=int(input("informe sua idade: "))


#Processamento e saída
if (idade<=17):
    print("Muito jovem para se aposentar")
elif(idade>=18 and idade <=65):
    print("Tem que trabalhar muito ainda!")
elif(idade>65):
    print("Se estiver vivo, pode aposentar!")
else:
    print("Idade inválida")

