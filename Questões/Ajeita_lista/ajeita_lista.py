# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação I
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Ajeita Lista
def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

lista = [3, 2, 1, 4, 5, 6, 7, 8, 9]

for i in range(0,len(lista) - 1, 2):
    if eh_par(lista[i]) == False and eh_par(lista[i + 1]) == True:
        lista[i], lista[i + 1] = lista[i + 1], lista[i]
for i in range(0,len(lista) - 1):
    if eh_par(lista[i]) == False and eh_par(lista[i + 1]) == True:
        lista[i], lista[i + 1] = lista[i + 1], lista[i]

print lista
