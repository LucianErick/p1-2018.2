#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Tinta

altura = float(raw_input())
largura = float(raw_input())

metros_por_litro = 13.8888 #descobre-se tal valor a partir de uma regra de três simples, onde: se 3.6 litros equivalem a 50 m2, 1 litro equivale a 13.888 m2
area = altura * largura

litros_de_tinta = area / metros_por_litro

print '%.2f l' % litros_de_tinta
