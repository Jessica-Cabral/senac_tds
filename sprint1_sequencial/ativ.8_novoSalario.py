'''Como funcionário quero informar meu salário e percentual de reajuste para saber qual meu novo salário.

• Critério 1 - Formas de Representação: Python. 

• Critério 2 - Dados de Entrada: salário, reajuste. 

• Critério 3 – Cálculo: reajuste = (salário*reajustes) /100, novo salário = salário + reajuste. 

• Critério 4 – Mensagem: “O novo salário é R$, novo salário”. Sendo que novo salário deve ser substituído pelo cálculo.'''

#Entrada
salario=float(input("Informe o salário: "))
percentualReajuste=float(input("Informe o percentual de reajuste: "))

#Processamento
valorReajuste=(salario*percentualReajuste)/100
novoSalario=salario+valorReajuste

#Saída
print("O novo salário é: ",novoSalario)