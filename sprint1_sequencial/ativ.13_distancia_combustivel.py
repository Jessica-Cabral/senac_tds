'''Como motorista quero saber a distância e a quantidade de combustível para chegar ao local desejado.

• Critério 1 - Formas de Representação: Python. 

• Critério 2 - Dados de Entrada: tempo gasto e velocidade média. 

• Critério 3 – Cálculo: distância = tempo gasto * velocidade média. 

• Critério 4 - Consumo: 12Km/L 

• Critério 5 – Cálculo: combustível gasto = distância/12 

• Critério 6 – Mensagem: “A distância é: ", distância, "e a quantidade de combustível é: ", combustível gasto.'''

#Entrada
tempoGasto=float(input("Informe o tempo gasto pelo motorista: "))
velocidadeMedia=float(input("Informe a velocidade média do motorista: "))

#Processamento
consumoCarro=12
distancia=tempoGasto*velocidadeMedia
combustivelGasto=distancia/consumoCarro


#Saída
print("A distâcia é: ",distancia)
print("A quantidade de combustível é: ",combustivelGasto)
