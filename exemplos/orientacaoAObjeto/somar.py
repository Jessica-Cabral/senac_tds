class Soma:
    
    def __init__(self):
        self.numero1 = None
        self.numero2 = None
    
    def getnumero1(self):
        return self.numero1
    
    def setnumero1(self, numero_1):
        self.numero1 = numero_1
        
    def getnumero2(self):
        return self.numero2
    
    def setnumero2(self, numero_2):
        self.numero2 = numero_2
        
    def Somar(self):
        return self.getnumero1()+self.getnumero2
    
#somar

obj_soma = Somar()
obj_soma.setnumero1(3)
obj_soma.setnumero2(5)
print (obj_soma.Somar())


