# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Quadrado na circunferência

import math

raio = float(raw_input())
lado = raio * math.sqrt(2.0)

circunferencia = math.pi * raio ** 2
quadrado = lado ** 2

area_nao_comum = circunferencia - quadrado

print 'Área não comum: %.5f' % area_nao_comum
