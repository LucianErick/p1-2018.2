# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação I | 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Conta Alertas

def conta_alertas_acude(medicoes):

    alarme = 0
    for i in range(2, len(medicoes)):

        vizinho = medicoes[i - 1]

        if abs(medicoes[i] - vizinho) <= 10:

            if medicoes[i] < 17:

                alarme += 1

    return alarme

medicoes = [50, 50, 50, 23, 21, 17, 15, 60, 65, 15, 15]
assert conta_alertas_acude(medicoes) == 2
