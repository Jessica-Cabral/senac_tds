class ContaBancaria:
    def __init__(self):
        self.numero_conta = None
        self.saldo = 0

    def get_numero_conta(self):
        return self.numero_conta

    def set_numero_conta(self, valor):
        self.numero_conta = valor

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, valor):
        self.saldo = valor
        
    def realizar_deposito(self,valor):
        self.set_saldo(self.get_saldo()+valor)
        
    def realizar_saque(self,valor):
        if self.get_saldo() >= valor:
            self.set_saldo(self.get_saldo()-valor)
        else:
            print("Saldo insuficiente!")
            
    def mostrar_saldo(self):
        print ("Saldo da conta:", self.get_saldo())
