# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: CPF

parte1 = int(raw_input())
parte2 = int(raw_input())
parte3 = raw_input()

digito_verificador = int(parte3[0]) + int(parte3[1]) + int(parte3[2])

print '%d.%d.%s-%02d' % (parte1, parte2, parte3, digito_verificador)
