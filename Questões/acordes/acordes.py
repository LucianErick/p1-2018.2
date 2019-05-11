# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação I
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Acordes Aprendidos

def my_in(elemento, lista):

    for i in range(len(lista)):
        if lista[i] == elemento:
            return True
    return False

def acordes(musica_1, musica_2):
    aprendidos = []

    if len(musica_1) != 0:
        for nota in musica_1:
            aprendidos.append(nota)

    if len(musica_2) != 0:
        for nota in musica_2:

            if my_in(nota, musica_1) == False:
                aprendidos.append(nota)

    return aprendidos
