# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação I | 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Inverte 2 a 2

def inverte2a2_condicional(seq):

    if len(seq) != 0:
        if len(seq) % 2 == 0:
            for i in range(0, len(seq) - 1, 2):
                if seq[i + 1] < seq[i]:
                    seq[i], seq[i + 1] = seq[i + 1], seq[i]

        else:
            for j in range(0,len(seq) - 2, 2):
                if seq[j + 1] < seq[j]:
                    seq[j], seq[j + 1] = seq[j + 1], seq[j]
