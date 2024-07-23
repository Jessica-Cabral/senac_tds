'''Como pesquisador quero informar uma pesquisa entre os habitantes de uma região para coletar para coletar mostrar média da idade do grupo, média da altura dos homens das mulheres, média da idade dos homens e da mulheres e percentual de pessoas com idade entre 18 e 35 anos (inclusive). 
• Critério 01 – Dados de Entrada: sexo (F - Feminino, M - Masculino), idade e altura de 100 pessoas. 
• Critério 02 – Condição: O sistema deve apresentar na tela: Digite o sexo da Xª pessoa. Onde X é o número da pessoa. O usuário deve informar o sexo da pessoa. 
• Critério 03 – Condição: O sistema deve apresentar na tela: Digite a idade da Xª pessoa. Onde X é o número da pessoa. O usuário deve informar a idade da pessoa. 
• Critério 04 – Condição: O sistema deve apresentar na tela: Digite a altura da Xª pessoa. Onde X é o número da pessoa. O usuário deve informar a altura da pessoa. 
• Critério 05 – Validação 1: O sistema só pode receber como entrada do sexo M ou F. Caso contrário mostrar a Mensagem 5. 
• Critério 06 – Validação 2: O sistema só pode receber como entrada idade maior ou igual a zero e menor que 120 anos. Caso contrário mostrar a Mensagem 6. 
• Critério 07 – Validação 3: O sistema só pode receber como entrada altura maior que zero e menor que 2,50 metros. Caso contrário mostrar a Mensagem 7. 
• Critério 08 – Resultado: após informar os dados das 100 pessoas, o sistema deve mostrar a Mensagem 1, Mensagem 2, Mensagem 3 e Mensagem 4. 
• Critério 09 – Mensagem 1: “A média da idade do grupo é:”, media. 
• Critério 10 – Mensagem 2: “A média da altura dos homens é:”, média homem. 
• Critério 11 – Mensagem 3: “A média da altura das mulheres é:”, média mulher. 
• Critério 12 – Mensagem 4: “O percentual de pessoas com idade entre 18 e 35 anos é:”, percentual. 
• Critério 13 – Mensagem 5: “Sexo inválido!” 
• Critério 14 – Mensagem 6: “Idade inválida!” • Critério 15 – Mensagem 7: “Altura inválida!”'''

#inicializar
i = 1
idade = 0
contPessoas = 0
somaIdade = 0
somaIdadeMulher = 0
quantidadeMulher = 0
somaIdadeHomem = 0
quantidadeHomens = 0
mediaIdade = 0
somaAlturaHomem = 0
somaAlturaMulher = 0
percentual = 0

#entrada e processamentos

while i <= 101:
    sexo = input("\nDigite o sexo M ou F da " + str(i) + "ª pessoa: ")

    while sexo != "M" and sexo != "m" and sexo != "F" and sexo != "f":
        sexo = input("Sexo inválido! \n Digite novamente M ou F: ")

    idade = int(input("Digite a idade da " + str(i) + "ª pessoa: "))

    while idade < 0 or idade > 127:
        idade = int(input("Idade inválida! \n Digite idade entre 0 e 127 anos: "))

    altura = float(input("Digite a altura da " + str(i) + "ª pessoa: "))

    while altura < 0 or altura > 2.5:
        altura = float(input("Altura inválida! \n Digite altura entre 0 e 2.5m: "))

    i += 1
    #somador das idades
    somaIdade += idade

    #somador e contador de idade mulher e idade homem
    if sexo == "F" or sexo == "f":
        quantidadeMulher += 1
        somaIdadeMulher += idade
        somaAlturaMulher += altura
    else:
        quantidadeHomens += 1
        somaIdadeHomem += idade
        somaAlturaHomem += altura

    #percentual
    if idade >= 18 and idade <= 35:
        contPessoas += 1

mediaIdade = somaIdade / (quantidadeHomens + quantidadeMulher)
mediaAlturaHomem = somaAlturaHomem / quantidadeHomens
mediaAlturaMulher = somaAlturaMulher / quantidadeMulher
percentual = (contPessoas * 100) / (quantidadeHomens + quantidadeMulher)

#saida
print("A média da idade do grupo é:", round(mediaIdade, 2))
print("A média da altura dos homens é:", round(mediaAlturaHomem, 2))
print("A média da altura das mulheres é:", round(mediaAlturaMulher, 2))
print("O percentual de pessoas com idade entre 18 e 35 anos é:", round(percentual, 2))

