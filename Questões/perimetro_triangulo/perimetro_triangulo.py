#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Perímetro triângulo

#Sabemos que o x representa eixo das abscissas (horizontal)
#Sabemos que o y representa o eixo das ordenadas (vertical)
#Logo, com conhecimento prévio, ao vermos o referencial do plano cartesiano deste jeito: (X,Y), concluímos então que isso representa: (a coordenada horizontal, a coordenada vertical)
import math

x1 = int(raw_input())
y1 = int(raw_input())
x2 = int(raw_input())
y2 = int(raw_input())
x3 = int(raw_input())
y3 = int(raw_input())

AB = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) 
BC = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
AC = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)

perimetro = AB + BC + AC

print 'O perímetro é de %.2f' % perimetro
