# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Diagonais 

lados = int(raw_input())

diagonais = lados * (lados - 3) / 2

print '%i lados => %i diagonais' % (lados, diagonais)
