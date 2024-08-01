from funcionario import Funcionario

func = Funcionario()
func.ler_dadosAcesso()

if func.validar_senha() == True:
    func.ler_dados()
    
else:
    print('Acesso negado!')