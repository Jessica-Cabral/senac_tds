'''Como usuário quero informar o código da peça, quantidade de peças e valor da peça para saber o valor total da quantidade de peças vendidas .
• Critério 1: Entrada de Dados: O sistema deve permitir que o usuário informe o código da peça, quantidade de peças e valor unitário da peça 
• Critério 2: Calculo: totalpecas = quantpecas*valorpeca 
• Critério 3: Exibição do Resultado: O sistema deve exibir o total de forma clara e legível para o usuário como exemplo abaixo: Código da peça: .............código da peça
    Valor da peça: R$............valor unitário da peça 
    Quantidade de peças: .... quantidade de peças 
    Valor total das peças: .... totalpecas'''

#Entrada
idPeca=int(input("Informe o código da peça: "))
qtdPecas=int(input("Informe a quantidade de peças: "))
valorPeca=float(input("Informe o valor unitário da peça: "))

#Processamento e saída
valorTotalPecas=qtdPecas*valorPeca

print("Código da peça_________________",idPeca)
print("Valor da peça__________________R$ ",valorPeca)
print("Quantidade de peças____________",qtdPecas)
print("Valor total das peças__________R$ ",valorTotalPecas)
