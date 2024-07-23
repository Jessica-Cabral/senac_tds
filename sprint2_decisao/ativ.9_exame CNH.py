'''Como usuário quero informar a idade e o resultado do exame mental para saber se estou apto a tirar carteira de motorista.
Critério 1 – Dados de Entrada: idade, resultadoExame
Critério 2 – Condição: se idade>18 anos e resultado= “sim”, está apto, mostrar a Mensagem 1. Senão, é menor de idade ou não foi aprovado no exame mental, mostrar a Mensagem 2. 
Critério 3 – Mensagem 1: “Apto”
Critério 4 – Mensagem 2: “Menor de idade/Não foi aprovado no exame mental”'''

#Entrada
idade=int(input("informe sua idade: "))
resultadoExame=str(input("informe o resultado do exame: "))


#Processamento e saída
if (idade>=18 and resultadoExame=="Sim"):
    print("Apto!")
else:
    print("Menor de idade ou Não foi aprovado no exame mental")

