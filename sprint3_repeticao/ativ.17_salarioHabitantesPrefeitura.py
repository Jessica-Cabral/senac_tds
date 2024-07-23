
'''Como prefeito quero fazer uma pesquisa entre os habitantes para saber a média do salário da população, média do número de filhos e percentual de pessoas com salário acima e abaixo do salário mínimo. 
• Critério 01 – Dados de Entrada: salário e número de filhos
• Critério 02 – Condição: O sistema deve apresentar na tela: Digite o salário. O usuário deve informar o salário.
• Critério 03 – Condição: O sistema deve apresentar na tela: Digite a quantidade de filhos. O usuário deve informar a quantidade de filhos. 
• Critério 04 – Condição: O sistema deve perguntar se deseja sair. Quando a opção for “s” o sistema deve sair e mostrar a Mensagem 1, Mensagem 2, Mensagem 3 e Mensagem 4. Se a opção for “n” o sistema deve continuar solicitando os dados de entrada. 
• Critério 05 – Validação 1: O sistema só pode receber como entrada salários maiores que zero.
• Critério 06 – Validação 2: O sistema só pode receber como entrada idades maiores ou igual a 0.
• Critério 07– Validação 3: O sistema só pode receber opção como entrada “s” ou “n”. Caso não seja um desses caracteres mostrar a mensagem 4.
• Critério 08 – Mensagem 1: “A média do salário da população é:”, média salário. 
• Critério 09 – Mensagem 2: “A média do número de filhos é:”, média filhos.
• Critério 10 – Mensagem 3: “O percentual de pessoas com salário abaixo do salário mínimo de R$ 1.412:”, percentual abaixo.
• Critério 11 – Mensagem 4: “O percentual de pessoas com salário acima do salário mínimo de R$ 1.412:”, percentual acima.'''    
    
totalPessoas = 0
somaSalarios = 0
somaFilhos = 0
contSalarioMaior = 0
contSalarioMenor = 0
opcaoSair = " "

# Salário mínimo 2024
salarioMinimo = 1412  

while (opcaoSair != "s"):
    while True:
        try:
            salario = float(input("Digite o salário: "))
            if salario <= 0:
                print("Salário inválido! O salário deve ser maior que zero.")
                continue

            filhos = int(input("Digite o número de filhos: "))
            if filhos < 0:
                print("Número de filhos inválido! Deve ser um número inteiro maior ou igual a zero.")
                continue
            
            totalPessoas += 1
            somaSalarios += salario
            somaFilhos += filhos

            if (salario < salarioMinimo):
                contSalarioMenor += 1
            else:
                contSalarioMaior += 1
                
            #validação para sair do sistema   
            opcaoSair = input("Deseja sair? (s/n): ").lower()
            if (opcaoSair=="s"):
                break
            elif(opcaoSair!="s"):
                continue
            else:
                print("Opção inválida! Digite 's' para sair ou 'n' para continuar.")

                    
        except ValueError:
            print("Valor inválido! Digite um número válido.")
            
if totalPessoas > 0:
    mediaSalario = somaSalarios / totalPessoas
    mediaFilhos = somaFilhos / totalPessoas
    percentualMenor = (contSalarioMenor / totalPessoas) * 100
    percentualMaior = (contSalarioMaior / totalPessoas) * 100

    print(f"A média do salário da população é: R${mediaSalario:.2f}")
    print(f"A média do número de filhos é: {mediaFilhos:.2f}")
    print(f"O percentual de pessoas com salário abaixo do salário mínimo de R$ {salarioMinimo:.2f}: {percentualMenor:.2f}%")
    print(f"O percentual de pessoas com salário acima do salário mínimo de R$ {salarioMinimo:.2f}: {percentualMaior:.2f}%")
else:
    print("Sem registro!")
