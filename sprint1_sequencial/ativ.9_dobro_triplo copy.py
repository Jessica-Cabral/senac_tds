'''Como usuário quero informar um número qualquer para saber dobro e o triplo do número informado.

• Critério 1 - Formas de Representação: Python. 

• Critério 2 - Dados de Entrada: número. 

• Critério 3 – Cálculo: dobro=número*2. 

• Critério 4 – Cálculo: triplo=número*3. 

• Critério 5 – Mensagem: “O dobro é, dobro, o triplo é, triplo”. Sendo que dobro e triplo devem ser substituídos pelo cálculo.'''

#Entrada
numero=float(input("Digite um número inteiro: "))

#Processamento
dobro=numero*2
triplo=numero*3

#Saída
print("O dobro é: ",dobro)
print("O triplo é: ",triplo)