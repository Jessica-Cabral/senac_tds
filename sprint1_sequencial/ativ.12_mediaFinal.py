'''Como professor quero informar as notas para obter a média final do aluno. 

• Critério 1 - Formas de Representação: Python. 

• Critério 2 - Dados de Entrada: nota 1, nota 2 e nota 3. 

• Critério 3 – Cálculo: media final= (nota 1 * 2 + nota 2 * 3 + nota 3 * 5) /10 

• Critério 4 – Mensagem: “A média final é: ", media final.'''

#Entrada
nota1=float(input("Informe a primeira nota do aluno: "))
nota2=float(input("Informe a segunda nota do aluno: "))
nota3=float(input("Informe a terceira nota do aluno: "))


#Processamento
mediaFinal=((nota1*2)+(nota2*3)+(nota3*5))/10

#Saída
print("A média final é: ",mediaFinal)
