'''Como vendedor quero calcular o meu salário para saber quanto irei receber.

• Critério 1 - Formas de Representação: Python. 

• Critério 2 - Dados de Entrada: quantidade carros vendidos, valor total vendas, salário fixo, valor por carro vendido. 

• Critério 3 – Cálculo: comissão vendas = valor fixo por carro vendido * quantidade carros vendidos 

• Critério 4 - Cálculo: comissão vendas fixo = valor total vendas * 0.05 

• Critério 5 – Salário: salário final = salário fixo + comissão vendas + comissão vendas fixo 

• Critério 6 – Mensagem: “O salário final é:", salário final.'''

#Entrada
totalCarrosVendidos=int(input("Informe o quantidade de carros vendidos: "))
valorTotalVendas=float(input("Informe o valor das vendas totais do vendedor: "))
salarioFixo=float(input("Informe o salário fixo do vendedor: "))
valorPorCarrosVendido=float(input("Informe o valor por carros vendido: "))

#Processamento
comissaoVenda=valorPorCarrosVendido*totalCarrosVendidos
comissaoVendaFixo=valorTotalVendas*0.05
salarioFinal=salarioFixo+comissaoVenda+comissaoVendaFixo

#Saída
print("O salário final é: ",salarioFinal)
