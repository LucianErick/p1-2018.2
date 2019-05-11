# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação I 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Área e Perímetro de um Círculo

import math

diametro = float(raw_input())
raio = diametro / 2
area = math.pi * raio ** 2
perimetro = 2 * math.pi * raio

print 'A: %.5f' % area
print 'P: %.5f' % perimetro
