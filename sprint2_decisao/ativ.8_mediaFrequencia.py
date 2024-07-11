'''Como usuário quero informar a média do aluno e a frequência para saber se ele foi aprovado ou reprovado. 
• Critério 1 – Dados de Entrada: media, frequência 
• Critério 2 – Condição: se a media >=5 e frequência>=70% aluno aprovado, mostrar a Mensagem 1. Senão aluno reprovado, mostrar a Mensagem 2. 
• Critério 3 – Mensagem 1: “Aluno aprovado!” 
• Critério 4 – Mensagem 2: “Aluno reprovado!”'''

#Entrada
media=float(input("informe media do aluno: "))
frequencia=float(input("informe a frequência do aluno: "))

#Processamento e saída
if (media>=5 and frequencia>70):
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")

