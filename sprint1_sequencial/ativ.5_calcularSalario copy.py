'''Como usuário quero calcular a área do quarto para saber se a cama irá caber.

• Critério 1 - Formas de Representação: Python. 

• Critério 2 - Dados de Entrada: largura e comprimento. 

• Critério 3 – Cálculo: área = largura X comprimento. • Critério 4 – Mensagem: “A área é”, área, “metros”. Sendo que área deve ser substituído pelo cálculo.'''

#Entrada
largura=float(input("Informe a largura: "))
comprimento=float(input("Informe o comprimento: "))

#Processamento
area=largura*comprimento

#Saída
print("A área é: ",area,"metros.")