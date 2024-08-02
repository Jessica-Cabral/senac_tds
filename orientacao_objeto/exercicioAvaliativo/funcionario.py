#Classe calcular quadrado ou retangulo

class Funcionario():
    def __init__(self):
        #atributos
        self.nome = None
        self.login = None
        self.senhaUsuario = None    
        self.senhaSistema = '1234'
        self.salario = None

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_login(self):
        return self.login

    def set_login(self, login):
        self.login = login

    def get_senhaUsuario(self):
        return self.senhaUsuario

    def set_senhaUsuario(self, senhaUsuario):
        self.senhaUsuario = senhaUsuario

    def get_senhaSistema(self):
        return self.senhaSistema

    def set_senhaSistema(self, senhaSistema):
        self.senhaSistema = senhaSistema

    def get_salario(self):
        return self.salario

    def set_salario(self, salario):
        self.salario = salario


    # ler dados
    
    def ler_dadosAcesso(self):
        self.set_login(input("Informe o Login: "))
        self.set_senhaUsuario(input("Informe a Senha: "))
                
    def ler_dados(self):
        self.set_nome(input("Informe o nome do funcionário: "))
        self.set_salario(float(input("Informe o Salário: ")))
    
    # validar senha
    
    def validar_senha(self):
        #self.set_senhaSistema('1234')
        if self.get_senhaUsuario() == self.get_senhaSistema(): 
            return True
        else: 
            return False
        
    #alterar senha
    
    def alterar_senha(self):
        self.set_senhaSistema(input("Informe a nova Senha: "))
        print('Senha alterada com sucesso!')
    
        
    #calcular IRPF
    
    def calcular_irpf(self):
        if self.get_salario() >= 2.500:
            return self.get_salario() * 0.15
        else:
            return 0
        
    #aumentar salário
      
    def aumentar_salario(self, percentualAumento):
        return self.set_salario(self.get_salario()+self.get_salario()*percentualAumento/100)
        
    #calcular salário
    
    def calcular_salario(self):
        self.set_salario(self.get_salario()-self.calcular_irpf())
        return print('Salário bruto: ',self.get_salario(),'\nDesconto IRPF: ', self.calcular_irpf(), '\nO novo salário é: ', self.get_salario())
    
    def cabecalho(self):
        print('--------------------------')
        print('        SISTEMA DP        ')
        print('--------------------------')
        
    def menuOpcao(self):
        print('--------------------------')
        print('        SISTEMA DP        ')
        print('--------------------------')
        print('\nEscolha uma opção:')
        print('1 - Cadastrar funcionário')
        print('2 - Mostrar dados')
        print('3 - Alterar Senha')
        print('4 - Calcular Salário')
        print('5 - Sair')
        opcao = input('Opcao: ')
        return opcao

    def mostrarDados(self):
        print('Nome: ', self.get_nome())
        print('Salário: ', self.get_salario())