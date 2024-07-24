lista_nomes = ['Maria','Marta','José','Pedro']

#Incluir nome
lista_nomes.append('Ana')

#Remover nome
lista_nomes.remove('Maria')

#numerar
for i, nome in enumerate(lista_nomes):
    print(i + 1,' - ',nome)
#Percorrer todas as posições
for nome in lista_nomes:
    print(nome)
