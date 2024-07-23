'''Como usuário quero informar a média do aluno para saber a situação do aluno.
• Critério 1 – Dados de Entrada: media
• Critério 2 – Condição: se media>=7, mostrar a mensagem 1. Se media>=5 e media<7, mostrar a mensagem 2. 
    Se media <5, mostrar mensagem 3.
• Critério 3 – Mensagem 1: “Aluno aprovado!”
• Critério 4 – Mensagem 2: “Aluno reprovado!”
• Critério 4 – Mensagem 3: “Aluno em recuperação.”'''

#Entrada
codigoLivro=str(input("Digite o código do livro: "))


#Processamento e saída
if (codigoLivro=="A"):
    print("A categoria é: ficção")
elif(codigoLivro=="B"):
    print("A categoria é: Não ficção")
else:
    print("Código inválido")

