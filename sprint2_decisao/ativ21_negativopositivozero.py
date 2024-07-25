'''Como usuário quero informar um número para saber se o número é positivo, negativo ou zero. 
Critério 1 – Dados de Entrada: numero 
Critério 2 – Condição: se número=0, mostrar a mensagem 1. Se número>0, mostrar a mensagem 2. Se número<0, mostrar a mensagem 3. 
Critério 3 – Mensagem 1: “Neutro” 
Critério 4 – Mensagem 2: “Positivo"
Critério 5 – Mensagem 3: “Negativo "'''

#Entrada
numero=float(input("Informe um número: "))


#Processamento e saída
if (numero==0):
    print("Neutro!")
elif(numero>0):
    print("Positivo")
elif(numero<0):
    print("Negativo")
else:
    print("Número inválido!")

