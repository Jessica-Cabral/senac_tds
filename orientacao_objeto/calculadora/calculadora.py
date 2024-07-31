#classe Calculadora

class Calculadora:

    #construtor
    def  __init__(self):
        #atributos
        self.numero1 = None
        self.numero2 = None
        self.operacoes = None
        
    #gets e sets
    def getnumero1(self):
        return self.numero1
    
    def setnumero1(self, numero_1):
        self.numero1 = numero_1
        
    def getnumero2(self):
        return self.numero2
    
    def setnumero2(self, numero_2):
        self.numero2 = numero_2   

    def getoperacoes(self):
        return self.operacoes
    
    def setoperacoes(self, operacao):
        self.operacoes = operacao 

    #somar
    def somar(self):
        return self.getnumero1()+self.getnumero2()

    #subtrair
    def subtrair(self):
        return self.getnumero1()-self.getnumero2()

    #multiplicar
    def multiplicar(self):
        return self.getnumero1()*self.getnumero2()

    #dividir
    def dividir(self):
        return self.getnumero1()/self.getnumero2()

    #calcular
    def calcular(self):
        if self.operacoes =='+':
            return self.somar()
        elif self.operacoes =='-':
            return self.subtrair()
        elif self.operacoes =='*':
            return self.multiplicar()
        elif self.operacoes =='/':
            return self.dividir()
        else:
            return 'Operação inválida!'