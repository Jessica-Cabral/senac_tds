'''Como usuário quero selecionar a opção para sair do sistema. 
• Critério 1 Dados de Entrada: opção 
• Critério 2 Condição: o sistema deve perguntar se deseja sair do sistema. Quando a opção for “s” o sistema deve fechar e se for “n” o sistema deve repetir a operação.'''

#inicializar
opcao = " "

while(opcao!="S" and opcao!="s"):
    opcao=str(input("Deseja sair do sistema? Digite S - Sair | N - Permancer no sistema\nOpção: "))


