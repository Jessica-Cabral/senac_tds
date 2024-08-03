from contaBancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    
    def __init__(self):
        #construtor da clase pai
        super().__init__()
        self.limite = 1000

    def get_limite(self):
        return self.limite

    def set_limite(self, valor):
        self.limite = valor
        
    def mostrar_saldo(self):
        print("Saldo da conta corrente:", self.get_saldo()+self.get_limite())