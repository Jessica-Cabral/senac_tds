
'''Como usuário quero informar a minha idade para saber quantos dias eu já vivi.

• Critério 1 - Formas de Representação: Python. 

• Critério 2 - Dados de Entrada: idade, mês e dia. 

• Critério 3 – Considerar ano com 365 dias e mês com 30 dias. 

• Critério 4 - Cálculo: dias_vividos = idade * 356 + mês * 30 + dia

• Critério 5 – Mensagem: “Você já viveu", dias_vividos.'''

#Funcão
def idade_em_dias():
    
    #Entradas
    idade=int(input("Informe a idade: "))
    mes_nascimento=int(input("Informe o mês de nascimento: "))
    dia_nascimento=int(input("informe o dia de nascimento: "))

    #Processamento
    dias_vividos=(idade*365)+(mes_nascimento*30)+dia_nascimento

    #Saída
    print("Você viveu",dias_vividos, "dias")
    
idade_em_dias()


