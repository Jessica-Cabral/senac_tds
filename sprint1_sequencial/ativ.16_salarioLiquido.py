'''Como contador quero calcular o salário líquido para apresentar ao funcionário 
• Critério 1 - Formas de Representação: Python. 
• Critério 2 - Dados de Entrada: salário bruto 
• Critério 3 – Cálculo: Imposto de Renda = salário bruto *0.11 
• Critério 3 – Cálculo: INSS = salário bruto *0.08 
• Critério 3 – Cálculo: sindicato = salário bruto *0.05 
• Critério 3 – Cálculo: salário líquido = salário bruto- (Imposto de Renda+INSS+sindicato) 
• Critério 6 – Mensagem:
“+ Salário Bruto: R$", salário bruto “- IR (11%): R$", Imposto de Renda 
“- INSS (8%): R$", INSS “- Sindicato (5%): R$", sindicato 
“= Salário Liquido: R$", salário liquido'''

#Entrada
salarioBruto=float(input("Informe o salário bruto do funcionário: "))

#Processamento
impostoDeRenda=salarioBruto*0.11
inss=salarioBruto*0.08
sindicato=salarioBruto*0.05
salarioLiquido=salarioBruto-(impostoDeRenda+inss+sindicato)

#Saída
print("+ Salário bruto: R$",salarioBruto," - IR(11%): R$ ",impostoDeRenda)
print("- INSS (8%): R$",inss," - sindicato(5%): R$ ",sindicato)
print("= Salário líquido: R$",salarioLiquido)

