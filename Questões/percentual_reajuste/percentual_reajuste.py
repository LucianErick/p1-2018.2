# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Percentual de reajuste

atual = float(raw_input('Valor atual? '))
novo = float(raw_input('Novo valor? '))

reajuste = ((novo - atual) / atual) * 100

print 'Reajuste de %.1f%%' % reajuste 
