#coding: utf-8

#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#UFCG - Programação 1
import math
print 'Cálculo da Superfície de um Cilindro'
print '---'
diametro = float(raw_input('Medida do diâmetro? '))
altura = float(raw_input('Medida da altura? ')) 
raio = diametro / 2

area_total = 2 * math.pi * raio * (raio + altura)
print '---'
print 'Área calculada: %.2f' % area_total 
