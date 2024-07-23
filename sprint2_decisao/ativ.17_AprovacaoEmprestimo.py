'''Como usuário eu quero informar valor do empréstimo, número de parcelas e salário do solicitante para saber se o empréstimo será aprovado 

• Critério 1 – Dados de Entrada: valor do empréstimo, número de parcelas e salário do solicitante. 

• Critério 2 – Condição: Aprovar empréstimo caso o valor de cada parcela represente no máximo 30% do salário do solicitante e mostrar a Mensagem 1. Senão a Mensagem 2.

 • Critério 3 – Mensagem 1: “Empréstimo aprovado!” 

• Critério 4 – Mensagem 2: "Empréstimo negado!"'''

#Entrada
salario=float(input("Informe o salário do solicitante: "))
valorEmprestimo=float(input("Informe o valor do empréstimo: "))
totalParcelas=int(input("Informe a quantidade de parcelas: "))

#Processamento e saída
parcela = valorEmprestimo/totalParcelas
if ((parcela/salario)<=0.3):
    print("Empréstimo aprovado")
else:
    print("Empréstimo não aprovado")

