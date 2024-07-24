#Teatro
teatro = [['L','L','L'],['L','L','L'],['L','L','L']]

#Reservar
teatro[0][0]='R'

#Cancelar
teatro[0][0]='L'

#Definir
teatro[0][0]= input("Digite L ou R")

#Mostrar em formato de teatro
for i, poltronas in enumerate(teatro):
    print("Fileira: ",i+1, " - ", poltronas)
    
#Mostrar em formato de teatro 2
for fileira in range(0,3):
    print()
    for coluna in range(0,3):
        print(teatro[fileira][coluna], end=" ") # testar enumerar as fileiras e colunas
        

#Mostrar
print(teatro)