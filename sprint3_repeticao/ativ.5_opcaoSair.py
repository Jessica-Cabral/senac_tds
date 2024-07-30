'''Como usuário quero selecionar uma opção para sair do sistema. 
• Critério 1 – Dados de Entrada: opção 
• Critério 2 – Condição: o sistema deve perguntar se deseja sair. Quando a opção for “s” o sistema deve sair e se for “n” o sistema deve continuar a operação. 
• Critério 3- Validação: o sistema só pode receber como entrada “s” ou “n”. Caso não seja um desses caracteres mostrar a mensagem.
 • Critério 3 – Mensagem: “Opção inválida.”'''



opcao = " "
#MENU

while(opcao!="S" or opcao!="s").lower():
    opcao=str(input("Deseja sair do sistema?\n[S] para sair  [N] para permanecer no sistema\nOpção: "))
    while(opcao!="S" or opcao!="N".lower())
        print ("Opção inválida digite uma opção valida")




