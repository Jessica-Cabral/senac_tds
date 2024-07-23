'''Como vendedor quero informar o meio de pagamento de um produto para saber qual desconto será aplicado e o valor final. 
• Critério 1: Dados de entrada: Valor do produto e tipo de pagamento. 
• Critério 2: Cálculo desconto de 10% para pagamento no cartão de crédito: desconto 10% = (Valor do produto- (valor do produto * 10%)) 
• Critério 3: Cálculo desconto de 15% para formas de pagamento em dinheiro à vista, débito ou Pix: desconto 15% = (Valor do produto-(valor do produto * 15%)) 
• Critério 4: mensagem: Deve-se retornar uma mensagem com o valor a pagar. Sendo que, se o pagamento for no cartão de crédito, o valor deve ser substituído pelo cálculo de desconto de 10%. Caso o pagamento seja em dinheiro à vista, débito ou Pix, o valor deve ser substituído pelo cálculo de desconto de 15%.'''

#Entrada
valorProduto=float(input("Informe o valor do produto: "))
tipoPagamento=str(input("Informe a forma de pagamento: dinheiro, debito, Pix ou credito: "))

#Processamento e saída
if (tipoPagamento=="crédito"):
    desconto=(valorProduto-(valorProduto*0.10))
    print("Valor a pagar: ", desconto)
else:
    desconto=(valorProduto-(valorProduto*0.15))
    print("Valor a pagar: ", desconto)

