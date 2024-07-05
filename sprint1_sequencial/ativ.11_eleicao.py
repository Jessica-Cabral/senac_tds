'''Como comissão eleitoral quero informar dados da eleição para verificar o resultado da eleição em percentual.

• Critério 1 - Formas de Representação: Portugol. 

• Critério 2 - Dados de Entrada: votos brancos, votos nulos e votos válidos. 

• Critério 3 - Cálculo 1: total votos = votos brancos + votos nulos + votos válidos. 

• Critério 4 - Cálculo 2: percentual brancos = (votos brancos*100) /total votos. 

• Critério 5 - Cálculo 3: percentual nulos = (votos nulos*100) /total votos. 

• Critério 6 - Cálculo 4: percentual válidos = (votos válidos*100) /total votos 

• Critério 7 – Mensagem: “Brancos: ", percentual brancos, "Nulos: ", percentual nulos, "Válidos: ", percentual válidos.'''

#Entrada
votosBrancos=int(input("Informe a quantidade de votos brancos: "))
votosNulos=int(input("Informe a quantidade de votos nulos: "))
votosValidos=int(input("informe a quantidade de votos válidos: "))

#Processamento
totalDeVotos=votosBrancos+votosNulos+votosValidos
percentualVotosBrancos=(votosBrancos/totalDeVotos)*100
percentualVotosNulos=(votosNulos/totalDeVotos)*100
percentualVotosValidos=(votosValidos/totalDeVotos)*100

#Saída
print("RESULTADO ELEIÇÃO:")
print("VOTOS BRANCOS: ",votosBrancos," - ",percentualVotosBrancos,)
print("VOTOS NULOS: ",votosNulos," - ",percentualVotosNulos)
print("VOTOS VÁLIDOS: ",votosValidos," - ",percentualVotosValidos)
