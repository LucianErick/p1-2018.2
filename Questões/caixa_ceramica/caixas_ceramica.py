# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Caixas de cerâmica

capacidade = float(raw_input('Capacidade de revestimento? '))
print
print '== Dados do vão a revestir =='
comprimento = float(raw_input('Comprimento? '))
largura = float(raw_input('Largura? '))
altura = float(raw_input('Altura? '))
print
print '== Resultados =='

paredes_laterais = 2 * largura * altura
paredes_frontais = 2 * comprimento * altura
chao = largura * comprimento

area = paredes_laterais + paredes_frontais + chao 

caixas = area / capacidade
print 'Área total a revestir: %.1f m2' % area
print 'Número de caixas: %i' % caixas
