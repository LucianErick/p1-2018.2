# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação I | 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: from

def separa_iguais(sequencia):
    sequencia = sequencia + ' '
    string = ''
    lista = []
    for i in range(1, len(sequencia)):

        vizinho = sequencia[i - 1]

        if sequencia[i] == vizinho:

            string += vizinho


        elif sequencia[i] != vizinho:
            string += vizinho
            lista.append(string)
            string = ''

    return lista

def char_unico(sequencia):

    for parte in separa_iguais(sequencia):

        if len(parte) == 1:

            return parte
