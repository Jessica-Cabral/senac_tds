'''Como usuário quero informar vários números para saber a soma entre eles. 

• Critério 1 – Dados de Entrada: numero 

• Critério 2 – Condição: Quando a opção for ‘s’ o sistema deve somar. Quando a opção for “n” o sistema deve fechar e mostrar a mensagem. 

• Critério 3 – Cálculo: soma = soma + numero 

• Critério 4 – Mensagem: “A soma é”, soma.'''

#inicializar
opcao = " "
resultadoSoma = 0

while(opcao!="s"):
    numero = float(input("Informe um número: "))
    opcao = str(input("Deseja saber o resultado da soma? \n Digite S/N: ")).lower()
    resultadoSoma +=numero

print("O resultado da soma é "+str(resultadoSoma))


