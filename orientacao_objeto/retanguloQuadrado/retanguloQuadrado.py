#Classe calcular quadrado ou retangulo

class Retangulo():
    def __init__(self):
        #atributos
        self.altura = None
        self.base = None
    
    
    def getAltura(self):
        return self.altura
    
    def setAltura(self, altura):
        self.altura = altura
    
    def getBase(self):
        return self.base
    
    def setBase(self, base):
        self.base = base
        
    # calcular área
    
    def calcularArea(self):
        return self.getBase() * self.getAltura()
    
    #verifica se é retangulo
    def verificarRetangulo(self):
        if self.getBase() == self.getAltura():
            return "quadrado"
        else:
            return "retângulo"
        
    
    
