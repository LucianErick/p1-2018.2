# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Calcula ingresso do cinema

adultos = int(raw_input())
criancas = int(raw_input())
ingresso = float(raw_input())

total = adultos * ingresso + criancas * (ingresso / 2)

print 'Total: R$ ' + str(total)
 
