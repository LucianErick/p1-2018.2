# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação I | 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Calculadora

while True:

    dados = raw_input().split(' ')

    tipo = dados[0]

    if tipo == '1':

        operacao = int(dados[1]) + int(dados[2])

    elif tipo == '2':

        operacao = int(dados[1]) - int(dados[2])

    elif tipo == '3':

        operacao = int(dados[1]) * int(dados[2])

    elif tipo == '4':

        if int(dados[2]) == 0:

            print 'Erro: Divisão por 0'

            break

        else:

            operacao = int(dados[1]) / int(dados[2])

    elif tipo == '5':

        break

    print operacao
