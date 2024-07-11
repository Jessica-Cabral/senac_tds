'''Como usuário quero informar a média do aluno para saber se ele foi aprovado ou reprovado.
• Critério 1 – Dados de Entrada: media 
• Critério 2 – Condição: se media>=5, aluno aprovado, mostrar a Mensagem 1. Senão, aluno reprovado, mostrar a Mensagem 2. 
• Critério 3 – Mensagem 1: “Aluno aprovado!” 
• Critério 4 – Mensagem 2: “Aluno reprovado!”'''

#Entrada
media=float(input("Digite a média do aluno: "))

#Processamento e saída
if (media>5):
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")

