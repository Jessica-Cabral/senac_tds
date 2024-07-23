'''Como usuário quero informar um número para saber se o número é maior que vinte e menor que 50. 
• Critério 1 – Dados de Entrada: numero 
• Critério 2 – Condição: se número=20, mostrar a mensagem 1, se número<20 e número>=50, mostrar a mensagem 2, se número>20 e número<50, mostrar a mensagem 3, 
• Critério 3 – Mensagem 1: “Este número é igual a vinte.” 
• Critério 4 – Mensagem 2: “Este número não está entre 20 e 50.” 
• Critério 5 – Mensagem 3: “Este número está entre 20 e 50.”'''

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

