#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1 | 2018.2
#Problema: Área de figuras planas

from math import pi

desenho = str(raw_input())
base = 0.0
lado = 0.0
raio = 0.0

if (desenho == "triângulo"):
	base = float(raw_input())
	lado = float(raw_input())
	triangulo = (base * lado) / 2.0
	print "Área do triângulo: %.2f (cm2)" % triangulo
elif (desenho == "quadrado"):
	lado = float(raw_input())
	quadrado = lado ** 2.0
	print "Área do quadrado: %.2f (cm2)" % quadrado
elif (desenho == "círculo"):
	raio = float(raw_input())
	circulo = pi * (raio ** 2)
	print "Área do círculo: %.2f (cm2)" % circulo
elif (desenho == "retângulo"):
	base = float(raw_input())
	lado = float(raw_input())
	retangulo = base * lado
	print "Área do retângulo: %.2f (cm2)" % retangulo
