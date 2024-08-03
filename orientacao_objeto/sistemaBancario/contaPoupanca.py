from contaBancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def __init__(self):
        super().__init__()
        self.taxa = None

    def get_taxa(self):
        return self.taxa

    def set_taxa(self, valor):
        self.taxa = valor
    
    def aplicar_juros(self,juros):
        self.set_saldo(self.get_saldo()+self.get_saldo()*juros/100)
    
    def mostrar_saldo(self):
        print("Saldo da Poupança:", self.get_saldo())
