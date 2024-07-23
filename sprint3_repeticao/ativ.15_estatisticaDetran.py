'''Como Detran quero informar as estatísticas das 200 principais cidades brasileiras para coletar dados sobre acidentes de trânsito.
 • Critério 01 – Dados de Entrada: código da cidade, estado, número de veículos de passeio e número de acidentes de trânsito com vítimas. 
 • Critério 02 – Condição: O sistema deve apresentar na tela: Digite o código da cidade. O usuário deve informar o código da cidade
 • Critério 03 – Condição: O sistema deve apresentar na tela: Digite o estado da cidade. O usuário deve informar o estado da cidade
 • Critério 04 – Condição: O sistema deve apresentar na tela: Digite o número de veículos da cidade. O usuário deve informar o número de veículos da cidade. 
 • Critério 05 – Condição: O sistema deve apresentar na tela: Digite o número de acidentes de carro. O usuário deve informar o número de acidentes de carro. 
 • Critério 06- Resultado: após informar as estatísticas das 200 principais cidades brasileiras, o sistema deve mostrar a Mensagem 1, Mensagem 2 e Mensagem 3.
 • Critério 07– Mensagem 1: “O maior e o menor índice de acidentes e a que cidades pertencem é:”, conceito. 
 • Critério 08 – Mensagem 2: “A média de veículos nas cidades brasileiras é:”, média.
 • Critério 09 – Mensagem 3: “Opção inválida!”'''
# Inicialização das variáveis
indiceAcidentesMaior = 0
indiceAcidentesMenor = 100000000000
cidadeMaiorIndice = " "
cidadeMenorIndice = " "
totalVeiculos = 0
totalAcidentes = 0

# Coleta dados das cidades
for i in range(1, 201):
    codigoCidade = input("Digite o código da cidade: ")
    estadoCidade = input("Digite o estado da cidade: ")
    totalVeiculos = int(input("Digite o número de veículos da cidade: "))
    totalAcidentes = int(input("Digite o número de acidentes de trânsito com vítimas: "))

    # Atualiza o maior e menor índice de acidentes e as cidades correspondentes
    if totalAcidentes > indiceAcidentesMaior:
        indiceAcidentesMaior = totalAcidentes
        cidadeMaiorIndice = f"{codigoCidade} - {estadoCidade}"
    if totalAcidentes < indiceAcidentesMenor:
        indiceAcidentesMenor = totalAcidentes
        cidadeMenorIndice = f"{codigoCidade} - {estadoCidade}"

    # Atualiza o total de veículos e acidentes
    totalVeiculos += totalVeiculos
    totalAcidentes += totalAcidentes

# Calcula a média de veículos nas cidades brasileiras
mediaVeiculos = totalVeiculos / 200

# Exibe os resultados
print(f"O maior e o menor índice de acidentes e a que cidades pertencem é:")
print(f"Maior índice de acidentes: {indiceAcidentesMaior} - {cidadeMaiorIndice}")
print(f"Menor índice de acidentes: {indiceAcidentesMenor} - {cidadeMenorIndice}")
print(f"A média de veículos nas cidades brasileiras é: {mediaVeiculos}")
