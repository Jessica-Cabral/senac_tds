'''Como usuário quero informar os votos da eleição para saber o resultado da eleição.
 • Critério 1 – Votos: Os votos são informados através de códigos. Os dados utilizados para a contagem dos votos obedecem à seguinte codificação: a) 1,2,3,4 = voto para os respectivos candidatos; b) 5 = voto nulo; c) 6 = voto em branco;
 • Critério 2 – Validação: A entrada de dados deve ser validada.
 • Critério 3 – Condição: O sistema deve apresentar na tela: Digite o voto: O usuário deve informar a opinião. O sistema deve repetir essa condição conforme o Critério 3. 
 • Critério 4 – Finalizar votação: O final da votação será indicado quando o voto for 0. O sistema deve mostrar a mensagem 1, mensagem 2, mensagem 3, mensagem 4 ou mensagem 5, conforme for o resultado. 
   Critério 5 – Mensagem 1: “Total de votos para cada candidato e percentual é:”, votos. 
 • Critério 6 – Mensagem 2: “Votos nulo e percentual é:”, nulo. • Critério 6 – Mensagem 3: “Votos em branco e percentual é:”, branco. 
 • Critério 7 – Vencedor: Se a soma dos votos nulos e brancos for maior que 50% dos votos, mostrar a mensagem 4, senão mostrar a mensagem 5. 
 • Critério 8 – Mensagem 4: “Eleição anulada!!!“
 • Critério 9 – Mensagem 5: “O candidato vencedor é:”, candidato. 
• Critério 10 – Senha: para mostrar o resultado da eleição o usuário deve informar a senha. Se a senha for errada o sistema não deve mostrar o resultado'''

#inicialização
votosCandidatos = {1: 0, 2: 0, 3: 0, 4: 0}
votosNulo = 0
votosBranco = 0

#menu
while True:
    print("\n_______________ELEICAO_____________________")
    print("Candidatos:")
    print("1 - Ana Clara")
    print("2 - Vaneiva Cunha")
    print("3 - Ana Paulo")
    print("4 - Jéssica Cabral")
    print("5 - Nulo")
    print("6 - Branco")
    print("0 - Resultado da votação")
    
    #input e acumulo dos votos
    voto = int(input("Digite o seu voto: "))
  
    if voto == 0:
        break
    elif voto not in [1, 2, 3, 4, 5, 6]:
        print("Voto inválido. Tente novamente.")
        continue
    
    if voto in [1, 2, 3, 4]:
        votosCandidatos[voto] += 1
    elif voto == 5:
        votosNulo += 1
    elif voto == 6:
        votosBranco += 1


senhaSistema = "12345"
senhaInserida = input("Informe a senha para acessar o resultado da eleição: ")

if senhaInserida == senhaSistema:
    totalVotos = sum(votosCandidatos.values()) + votosNulo + votosBranco

  
    percentualNulo = (votosNulo / totalVotos) * 100 if totalVotos > 0 else 0
    percentualBranco = (votosBranco / totalVotos) * 100 if totalVotos > 0 else 0

    if percentualNulo + percentualBranco > 50:
        print("Eleição anulada!!!")
    else:
    
        candidatoVencedor = max(votosCandidatos, key=votosCandidatos.get)
        print(f"O candidato vencedor é: Candidato {candidatoVencedor}")

    print("\nResultados da Eleição:")
    for candidato, votos in votosCandidatos.items():
        percentual = (votos / totalVotos) * 100 if totalVotos > 0 else 0
        print(f"Total de votos para {candidato}º candidato e percentual é: {votos} - {percentual:.2f}%")
    
    print(f"Votos nulo e percentual é: {votosNulo} - {percentualNulo:.2f}%")
    print(f"Votos em branco e percentual é: {votosBranco} - {percentualBranco:.2f}%")
else:
    print("Senha incorreta. Não é possível mostrar os resultados.")
