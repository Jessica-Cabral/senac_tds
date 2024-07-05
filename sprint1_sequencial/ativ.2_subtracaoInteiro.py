'''Como usuário quero informar três números inteiros para o obter o valor da subtração entre eles.

• Critério 1 - Formas de Representação: Python.

• Critério 2 - Dados de Entrada: n1, n2, n3 

• Critério 3 – Cálculo: sub=n1-n2-n3. 

• Critério 4 – Mensagem: “O resultado é subtração:”, sub. Sendo que sub deve ser substituído pelo valor calculado.'''

#Entrada
numero1=int(input("Digite o primeiro número: "))
numero2=int(input("Digite o segundo número: "))
numero3=int(input("Digite o terceiro número: "))

#Processamento
subtracao=numero1-numero2-numero3

#Saída
print("O resultado é: ",subtracao)