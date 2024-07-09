'''Como usuário quero informar a quantidade de apartamentos e desconto da diária para saber quanto arrecadarei no final de semana .
• Critério 1: Entrada de Dados: O sistema deve permitir que o usuário informe o número de apartamentos do hotel e o valor da diária por apartamento para o final de semana completo. 
• Critério 2: Regras: O sistema deve calcular valor promocional da diária; Valor total a ser arrecadado caso a ocupação neste final de semana atinja 100%; Valor total a ser arrecadado caso a ocupação neste final de semana atinja 70%; Valor que o hotel deixará de arrecadar em virtude da promoção, caso a ocupação atinja 100%. 
• Critério 3: Calculo: promodiaria=valordiaria*desc, 
• Critério 4: diariadesc=valordiaria-promodiaria 
• Critério 5: arrecadado100=valordiaria-promodiaria*napart,
• Critério 6: arrecadado70=(valordiaria-promodiaria*napart) *(0.70), 
• Critério 7: total=napart*valordiaria 
• Critério 8: Exibição do Resultado: O sistema deve exibir o total de forma clara e legível para o usuário como exemplo abaixo: 
    Número de apartamentos: número de apartamentos 
    Valor diária: R$
    Valor da diária (25%): R$ 
    Valor arrecadado (100%) ocupação com desconto: R$ 
    Valor arrecadado (70%) ocupação com desconto: 
    R$ valor não arrecadada ocupação (100%) em razão da promoção: R$ 
    Valor arrecadado (100%) e sem desconto: R$'''

#Entrada
totalApartamentos=int(input("Informe a quantidade total de apartamentos: "))
valorDiaria=float(input("Informe o valor da diária: "))


#Processamento e saída
valorDiaria25porcent = valorDiaria-(valorDiaria*0.25)
arrecadacaoTotal=valorDiaria*totalApartamentos


print("Número de apartamentos______________________________________R$",totalApartamentos)
print("Valor da diária_____________________________________________R$",valorDiaria)
print("Valor da diária (25%)_______________________________________R$",valorDiaria25porcent)
print("Valor arrecadado (100%) ocupação com desconto:______________R$",(totalApartamentos*valorDiaria25porcent))
print("Valor arrecadado (70%) ocupação com desconto:_______________R$",(totalApartamentos*valorDiaria25porcent)*0.7)
print("valor não arrecadada ocupação (100%) em razão da promoção:__R$",arrecadacaoTotal-(totalApartamentos*valorDiaria25porcent))
print("Valor arrecadado (100%) sem desconto:_______________________R$",(arrecadacaoTotal))

