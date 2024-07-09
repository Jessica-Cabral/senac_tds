'''Como vendedor quero calcular o consumo do cliente para ele efetuar o pagamento
• Critério 1 - Formas de Representação: Python. 
• Critério 2 - Dados de Entrada: quantidade Hambúrguer, quantidade Cheeseburger, quantidade Fritas, quantidade Refrigerante, quantidade Milkshake 
• Critério 3 – Cálculo: consumo = quantidade Hambúrguer*15+ quantidade Cheeseburger*12,50+quantidade Fritas*9,5+quantidade Refrigerante*7+ quantidade Milkshake*10 
• Critério 4 – Mensagem: 
“Hambúrguer................. R$", quantidade Hambúrguer*15
“Cheeseburger............... R$", quantidade Cheeseburger*12,50 
“Fritas................. .....R$", quantidade Fritas*9,5 
“Refrigerante.......... ......R$", quantidade Refrigerante*7 
“Milkshake........ ...........R$", quantidade Milkshake*10 
“Total.................... ...R$", consumo'''

#Entrada
qtdHambuguer=int(input("Informe a quantidade de hamburguer: "))
qtdCheeburguer=int(input("Informe a quantidade de cheeburguer: "))
qtdFritas=int(input("Informe a quantidade de fritas: "))
qtdRefrigerante=int(input("Informe a quantidade de refrigerante: "))
qtdMilkshake=int(input("Informe a quantidade de milkshake: "))

#Processamento e saída
consumo=(qtdHambuguer*15)+(qtdCheeburguer*12.5)+(qtdFritas*9.5)+(qtdRefrigerante*7)+(qtdMilkshake*10)
print("Hambuguer____________________R$ ",qtdHambuguer*15)
print("Cheeburguer__________________R$ ",qtdCheeburguer*12.5)
print("Fritas_______________________R$ ",qtdFritas*9.5)
print("Refrigerante_________________R$ ",qtdRefrigerante*7)
print("Milkshake____________________R$ ",qtdMilkshake*10)
print("Valor total__________________R$ ",consumo)
