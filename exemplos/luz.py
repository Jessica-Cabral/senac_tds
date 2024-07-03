nome = input("Digite o nome: ")
luz = float(input("Digite o valor da conta de luz: ")) # Valor da conta de luz
agua = float(input("Digite o valor da conta de água: ")) # Valor da conta de água
total = agua + luz # Soma dos valores de água e luz
netflix = float(input("Digite o valor da assinatura netflix: ")) # Valor da assinatura da Netflix
total += netflix # Atualiza o valor total
print("Total é: ",total)

