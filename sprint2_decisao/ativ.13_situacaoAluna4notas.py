'''Como professor quero informar as notas do aluno para saber a situação do aluno. 
• Critério 1: Dados de entrada: nota1, nota2, nota3 e nota4. 
• Critério 2: Cálculo média: media=((nota1+nota2+nota3+nota4) /4) 
• Critério 3: Cálculo avaliação e mensagem: Se média for maior ou igual a 7, deve retornar a mensagem “Aprovado!”. Caso a média seja menor que 7, deve retornar a mensagem “Reprovado!”.'''

#Entrada
nota1=float(input("Digite a nota 1: "))
nota2=float(input("Digite a nota 2: "))
nota3=float(input("Digite a nota 3: "))
nota4=float(input("Digite a nota 4: "))

#Processamento e saída
media=(nota1+nota2+nota3+nota4)/4

if (media>7):
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")

