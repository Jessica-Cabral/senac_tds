
'''Como usuário quero informar um número inteiro para saber a sua forma extensa.'''    
    

#funçao
def numero_extenso():
    numero = int(input("Informe um número: "))
    
    if (numero==0):
        return "Zero"
    elif (numero==1):
        return "Um"
    elif (numero==2):
        return "Dois"
    elif (numero==3):
        return "Três"
    elif (numero==4):
        return "Quatro"
    elif (numero==5):
        return "Cinco"
    elif (numero==6):
        return "Seis"
    elif (numero==7):
        return "Sete"
    elif (numero==8):
        return "Oito"
    elif (numero==9):
        return "Nove"
    elif (numero==10):
        return "Dez"
    else:
        return "Número inválido"
    
print("Por extenso o número é : " + str(numero_extenso()))
                




