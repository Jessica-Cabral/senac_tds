from funcionario import Funcionario
import os

func = Funcionario()
func.cabecalho()
func.ler_dadosAcesso()
os.system("cls")


if func.validar_senha() == True:
    opcao = func.menuOpcao()
    while  opcao != 4:
        if opcao == '1': #Cadastrar funcionário
            os.system("cls")
            func.cabecalho()
            func.ler_dados()
            print('Cadastro realizado sucesso!')
            os.system("pause")
            os.system("cls")
            opcao =func.menuOpcao()
        elif opcao == '2': #Apresentar dados do funcionário cadastrado
            os.system("cls")
            func.cabecalho()
            func.mostrarDados()
            os.system("pause")
            os.system("cls")
            opcao = func.menuOpcao()
        elif opcao == '3': #Alterar senha de acesso ao sistema
            os.system("cls")
            func.cabecalho()
            func.alterar_senha()
            os.system("pause")
            os.system("cls")
            opcao = func.menuOpcao()
        elif opcao == '4': #Calcular aumento salarial
            os.system("cls")
            func.cabecalho()
            func.ler_dados()
            func.aumentar_salario(float(input('Informe o percentual de aumento: ')))
            func.calcular_irpf()
            print (func.calcular_salario())
            os.system("pause")
            os.system("cls")
            opcao = func.menuOpcao()
        elif opcao == '5':
            os.system("cls")
            func.cabecalho()
            print('Sessão encerrada!')
        else:
            print('Opção inválida!')
            os.system("pause")
            func.menuOpcao()
else:
    func.cabecalho()
    print('Acesso negado!')