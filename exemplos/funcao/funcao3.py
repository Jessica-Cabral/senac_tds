
def meses(mes):
    if (mes==1):
        return "Janeiro"
    elif (mes==2):
        return "Fevereiro"
    elif (mes==3):
        return "Março"
    elif (mes==4):
        return "Abril"
    elif (mes==5):
        return "Maio"
    elif (mes==6):
        return "Junho"
    elif (mes==7):
        return "Julho"
    elif (mes==8):
        return "Agosto"
    elif (mes==9):
        return "Setembro"
    elif (mes==10):
        return "Outubro"
    elif (mes==11):
        return "Novembro"
    elif (mes==12):
        return "Dezembro"
    else:
        return "Mês inválido"
    


def meses_vet(mes):
    nome_meses = ['Inválido','Jan','Fev','Mar','Abr','Mai','Jun','jul']
    return nome_meses[mes]

    
print (meses(1))
print (meses(0))

print (meses_vet(2))
print (meses_vet(0))