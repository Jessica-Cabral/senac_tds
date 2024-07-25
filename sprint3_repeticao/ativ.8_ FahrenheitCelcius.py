
'''Como usuário quero informar a temperatura em graus Fahrenheit para transformar para graus Celsius 
• Critério 1 – Dados de Entrada: fahrenheit 
• Critério 2 – Condição: O sistema deve apresentar na tela a temperatura em Celsius correspondendo a variação de 1 a 50 em fahrenheit 
• Critério 3 – Cálculo: celsius = (fahrenheit - 32) * 5/9 
• Critério 4 – Mensagem: "ºF", fahrenheit, " = ºC", celsiu'''    
    

#Entrada

temperatuaFahrenheit = float(input("Informe a temperatura em fahrenheit: "))

#Processamento

converteCelsius = (temperatuaFahrenheit *1.8)+32

#saida

print(str(temperatuaFahrenheit)+"°F = "+str(converteCelsius)+"°C")