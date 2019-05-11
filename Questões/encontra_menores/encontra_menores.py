# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação I | 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Encontra Menores

def encontra_menores(numero, lista):

    lista_menores = []
    for valor in lista:

        if valor < numero:
            lista_menores.append(valor)

    if len(lista_menores) == 0:
        return - 1

    else:

        return lista_menores[0]

lista1 = [100,200,300,400]
lista2 = [15, 12, 4, 9, 10]
assert encontra_menores(100, lista1) == -1
assert encontra_menores(10, lista2) == 4
