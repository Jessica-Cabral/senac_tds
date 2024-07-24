#lista de inteiros
nome = []
nota1 = []
nota2 = []


#Entrada - informar alunos e notas

for i in range(0,2):
    nome.append(input("Digite o nome do " + str(i+1) +"º aluno: "))
    nota1.append(float(input("Digite a nota 1 do " + str(i+1) +"º nota aluno: ")))
    nota2.append(float(input("Digite a nota 2 do " + str(i+1) +"º nota aluno: ")))
  
    
    
#média
for i in range(0,2):
    media = (nota1[i]+nota2[i])/2
    if(media<=7):
        situacao = "Reprovado!"
    else:
        situacao = "Aprovado!"
    print("A nota do "+nome[i]+" é: "+str(media)+ " - Situação: "+situacao)
