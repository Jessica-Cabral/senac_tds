'''Como gerente quero informar a quantidade de carros vendidos, salário fixo e comissão das vendas do vendedor, para saber o salário final do vendedor.
• Critério 1: Entrada de Dados: O sistema deve permitir que o usuário informe quantidade de carros vendidos, valor total das vendas, o salário fixo, comissão fixa. 
• A comissão fixa é 5% do total das vendas
• Critério 2: Calculo: total = salarioFixo+(comissaoFixa/100*(quantCarros)) +(comissaoVendas*valorVendas) 
• Critério 3: Exibição do Resultado: O sistema deve exibir o salário de forma clara e legível para o usuário. 
• O salário deve ser apresentado como um número real.'''

#Entrada
totalCarrosVendidos=int(input("Informe a quantidade total de carros vendidos: "))
valorTotalVendas=float(input("Informe o valor total das vendas: "))
salarioFixo=float(input("Informe o salário fixo do vendedor: "))



#Processamento e saída

percentComissaoFixa=0.05
comissaoFixa=(valorTotalVendas*percentComissaoFixa)
comissaoFixaSobreTotalCarros=totalCarrosVendidos*comissaoFixa
comissaoVendas=valorTotalVendas*percentComissaoFixa
salarioFinal=salarioFixo+comissaoFixaSobreTotalCarros+comissaoVendas

print("Salário Fixo:______________________________R$",salarioFixo)
print("Comissão Fixa sobre carros vendidos:_______R$",comissaoFixaSobreTotalCarros)
print("Comissão Vendas:_____________R$",comissaoVendas)
print("Salário Final:_______________R$",salarioFinal)
