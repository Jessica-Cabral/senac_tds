#importar a class calculadora

from orientacao_objeto.calculadora.calculadora import Calculadora

#criar o objeto (instancia)

calculadora = Calculadora()
calculadora.setnumero1(float(input('Digite o número 1: ')))
calculadora.setnumero2(float(input('Digite o número 2: ')))
calculadora.setoperacoes(input('[+] somar [-] subtrair [*] multiplicar [/] dividir - Digite a operação: '))
print('Resultado: ',calculadora.calcular())
