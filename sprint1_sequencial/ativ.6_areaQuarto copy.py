'''Como usuário quero calcular o meu salário para saber quanto posso gastar no mês.

• Critério 1 - Formas de Representação: Python. 

• Critério 2 - Dados de Entrada: quantidade de horas. 

• Critério 3 – Cálculo: salário = R$ 30,00 x quantidade de horas. 

• Critério 4 – Mensagem: “O salário é: R$ “, salário. Sendo que salário deve ser substituído pelo cálculo.'''

#Entrada
horasTrabalhadas=float(input("Digite a quantidade de hpras trabalhadas: "))

#Processamento
salario=30*horasTrabalhadas

#Saída
print("O salário é: ",salario)