'''Como usuário quero informar a altura e sexo de uma pessoa para saber o seu peso ideal 
• Critério 1 – Dados de Entrada: altura e sexo 
• Critério 2 – Condição: se o sexo for “H”, calcular o peso ideal para homens e mostrar a Mensagem 1. Senão, peso ideal para mulheres e mostrar a Mensagem 2. 
Para homens: Peso ideal (P) = (72,7 * H) – 58 
Para mulheres: Peso ideal (P) = (62,1 * H) – 44,7 
• Critério 3 – Mensagem 1: “O peso ideal para homens é de:”, Peso ideal 
• Critério 4 – Mensagem 2: “O peso ideal para mulheres é de:”, Peso ideal'''

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

