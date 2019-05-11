#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Percentual de reajuste do salário mínimo

valor_atual = float(raw_input('Valor atual? '))
novo_valor = float(raw_input('Novo valor? '))

percentual_reajuste = ((novo_valor - valor_atual) / valor_atual) * 100
print 'Reajuste de %.1f%%' % percentual_reajuste   
