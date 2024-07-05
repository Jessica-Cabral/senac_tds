'''Como usuário quero informar a minha idade para saber quantos dias eu já vivi.

• Critério 1 - Formas de Representação: Python. 

• Critério 2 - Dados de Entrada: idade, mês e dia. 

• Critério 3 – Considerar ano com 365 dias e mês com 30 dias. 

• Critério 4 - Cálculo: dias_vividos = idade * 356 + mês * 30 + dia

• Critério 5 – Mensagem: “Você já viveu", dias_vividos.'''

#Entrada
idade=int(input("Informe a idade: "))
mesNascimento=int(input("Informe o mês de nascimento: "))
diaNascimento=int(input("informe o dia de nascimento: "))

#Processamento
diasVividos=(idade*365)+(mesNascimento*30)+diaNascimento

#Saída
print("Você viveu ",diasVividos)
