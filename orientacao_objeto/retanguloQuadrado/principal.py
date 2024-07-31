from retanguloQuadrado import Retangulo

area = Retangulo()
area.setAltura(float(input('Informe a altura: ')))
area.setBase(float(input('Informe a base:')))
print('A área total é de ', area.calcularArea(), 'e corresponde a um ', area.verificarRetangulo())