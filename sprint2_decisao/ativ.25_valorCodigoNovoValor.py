'''CComo usuário quero informar o valor de um produto e código de aumento para saber o valor do produto.

Critério 1 - Dados de entrada: valor do produto e código de aumento
Critério 2 -  Regra - Tabela de aumento: O novo valor do produto acrescido e calculado de acordo com a tabela de aumento abaixo.
Critério 3 -  Cálculo - Novo valor: valor do produto + (valor do produto * % aumento).
Critério 4 - Mensagem: “O novo valor do produto é, novo valor. Sendo que o novo valor deve ser substituído pelo cálculo.'''

#Entrada
valorProduto=float(input("Informe o valor do produto: "))
input("% DESCONTO\n1 - 15% de desconto\n3 - 20% de desconto\n5 - 25% de desconto\n7 - 30% de desconto")
codigoDesconto=int(input("\nInforme o código e desconto: "))


#Processamento e saída
if (codigoDesconto==1):
    novoValor=(valorProduto-(valorProduto*0.15))
    print("O novo valor do produto é, R$ "+str(novoValor))
elif(codigoDesconto==3):
    novoValor=valorProduto-(valorProduto*0.20)
    print(("O novo valor do produto é, R$ "+str(novoValor)))
elif(codigoDesconto==5):
    novoValor=valorProduto-(valorProduto*0.25)
    print("O novo valor do produto é, R$ "+str(novoValor))
elif(codigoDesconto==7):
    novoValor=valorProduto-(valorProduto*0.30)
    print("O novo valor do produto é, R$ "+str(novoValor) )
else:
    print("Código inválido!")

