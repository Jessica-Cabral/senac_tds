'''Como usuário quero informar o custo de fábrica e porcentagens do distribuidor, impostos, e comissão do vendedor para saber o custo final do consumidor 
• Critério 1: Entrada de Dados: O sistema deve permitir que o usuário informe o custo de fábrica e porcentagens do distribuidor, impostos, e comissão do vendedor 
• Critério 2: Calculo: custoDistribuidor = custoFabrica*percentualDistribuidor, 
• Critério 3: Calculo: impostos = custoFabrica*percentualImpostos, 
• Critério 4: Calculo: comissaoVendedor=custoFabrica*percentualComissao, 
• Critério 5: Calculo: custoFinal=custoFabrica+impostos+custoDistribuidor 
• Critério 6: Exibição do Resultado: O sistema deve exibir o total de forma clara e legível para o usuário como exemplo abaixo: Custo de fábrica...........R$ custo de fábrica 
    Distribuidor.................R$ distribuidor
    Impostos.....................R$ impostos 
    Custo final...................R$ custoFinal
    Comissão vendedor: R$ totalcomissaovendedor'''

#Entrada
custoFabrica=float(input("Informe o custo de fábrica: "))
percentualDistribuidor=float(input("Informe a porcentagem do distribuidor: "))
percentualImpostos=float(input("Informe a porcentagem dos impostos:  "))
percentualComissao=float(input("Informe a porcentagem da comissão do vendedor: "))

#Processamento e saída
impostos = custoFabrica*percentualImpostos
custoDistribuidor = custoFabrica*percentualDistribuidor
comissaoVendedor=custoFabrica*percentualComissao
custoFinal=custoFabrica+impostos+custoDistribuidor

print("Custo de fábrica_________________R$",custoFabrica)
print("Distribuidor_____________________R$",custoDistribuidor)
print("Impostos_________________________R$",impostos)
print("Custo final______________________R$",custoFinal)
print("Comissão vendedor________________R$",comissaovendedor)
