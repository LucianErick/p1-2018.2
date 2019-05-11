# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação I | 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Divisor

def divisor(numero, lista):

    lista_divisores = []
    for i in range(len(lista)):

        if (lista[i] % numero) == 0:

            lista_divisores.append(lista[i])

        if len(lista_divisores) != 0:

            return i

    if len(lista_divisores) == 0:

        return -1        
