# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação I
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Afinidade Musical

def my_in(elemento, lista):

    for i in range(len(lista)):
        if lista[i] == elemento:
            return True
    return False

def tem_afinidade(l1, l2):
    matchs = 0
    for dado in l2:
        if my_in(dado, l1) == True:
            matchs += 1

    if matchs >= 3:
        return True
    else:
        return False
