# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Perímetro de um Triângulo

import math

x1 = int(raw_input()) # ponto a
y1 = int(raw_input()) 

x2 = int(raw_input()) # ponto b
y2 = int(raw_input()) 

x3 = int(raw_input()) # ponto c
y3 = int(raw_input()) 

ab = math.sqrt((x1 * 1.0 - x2) ** 2 + (y1 - y2) ** 2) 
bc = math.sqrt((x2 * 1.0 - x3) ** 2 + (y2 - y3) ** 2)
ac = math.sqrt((x1 * 1.0 - x3) ** 2 + (y1 - y3) ** 2)

perimetro = ab + bc + ac

print 'O perímetro é de %.2f' % perimetro
