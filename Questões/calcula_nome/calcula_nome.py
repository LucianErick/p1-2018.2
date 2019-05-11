# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Calcula Nome

nome = raw_input('Nome? ')
letra = float(raw_input('Letra? R$ '))

orcamento = len(nome) * letra

print 'Orçamento: R$ %.1f' % orcamento 
