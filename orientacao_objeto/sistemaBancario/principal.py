from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupanca




#conta corrente

cc = ContaCorrente()
cc.set_saldo(0)
cc.realizar_deposito(float(input("Informe o valor do deposito: ")))
cc.mostrar_saldo()
cc.realizar_saque(float(input("Informe o valor do saque: ")))
cc.mostrar_saldo()

#conta poupança
'''cp = ContaPoupanca()
cp.realizar_deposito = ((input("Informe o valor do deposito: ")))
cp.mostrar_saldo()
cp.realizar_saque = ((input("Informe o valor do saque: ")))
cp.mostrar_saldo()'''