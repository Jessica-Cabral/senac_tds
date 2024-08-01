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
        if self.get_senhaUsuario == self.get_senhaSistema(): 
            return True
        else: 
            return False
        
    #calcular IRPF
    
    def calcular_irpf(self):
        if self.get_salario() >= 2.500:
            return self.get_salario() * 0.15
        else:
            return 'Isento!'
        
    #aumentar salário
    
    def aumentar_salario(self, percentualAumento):
        self.set_salario()+(self.get_salario()*percentualAumento)
        return self.get_valorAumento()
       
    #calcular salário
    
    def calcular_salario(self):
        self.set_salario()- self.calcular_irpf()
        return self.get_novoSalario()