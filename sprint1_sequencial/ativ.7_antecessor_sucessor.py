'''Como usuário quero informar um número inteiro qualquer para saber o antecessor e sucessor.

• Critério 1 - Formas de Representação: Python. 

• Critério 2 - Dados de Entrada: número. • Critério 3 – Cálculo: antecessor = número -1, sucessor=número+1. 

• Critério 4 – Mensagem: “O antecessor é”, antecessor, “o sucessor é”, sucessor. Sendo que antecessor e sucessor deve ser substituído pelo cálculo.'''

#Entrada
numero=int(input("Digite um número inteiro: "))

#Processamento
antecessor=numero-1
sucessor=numero+1

#Saída
print("O antecessor é: ",antecessor)
print("O sucessor é: ",sucessor)