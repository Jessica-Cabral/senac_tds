'''Como usuário quero informar a média do aluno para saber a situação do aluno.
• Critério 1 – Dados de Entrada: media
• Critério 2 – Condição: se media>=7, mostrar a mensagem 1. Se media>=5 e media<7, mostrar a mensagem 2. 
    Se media <5, mostrar mensagem 3.
• Critério 3 – Mensagem 1: “Aluno aprovado!”
• Critério 4 – Mensagem 2: “Aluno reprovado!”
• Critério 4 – Mensagem 3: “Aluno em recuperação.”'''

#Entrada
media=float(input("Digite a média do aluno: "))


#Processamento e saída
if (media>=5 and media<7):
    print("Aluno em recuperação!")
elif(media>=7):
    print("Aluno Aprovado!")
else:
    print("Aluno reprovado!")

