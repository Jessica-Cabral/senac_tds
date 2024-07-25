
'''Como usuário quero informar a temperatura em graus Fahrenheit para transformar para graus Celsius 
• Critério 1 – Dados de Entrada: fahrenheit 
• Critério 2 – Condição: O sistema deve apresentar na tela a temperatura em Celsius correspondendo a variação de 1 a 50 em fahrenheit 
• Critério 3 – Cálculo: celsius = (fahrenheit - 32) * 5/9 
• Critério 4 – Mensagem: "ºF", fahrenheit, " = ºC", celsiu'''    
    

#funçao
def converter_celsiusParaFahrenheit():
    
    temperatuaFahrenheit = float(input("Informe a temperatura em fahrenheit: "))
    converteCelsius = (temperatuaFahrenheit *1.8)+32
    print(str(temperatuaFahrenheit)+"°F = "+str(converteCelsius)+"°C")
    
#invocar

converter_celsiusParaFahrenheit()



