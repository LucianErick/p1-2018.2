#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Validação de triângulos

a = int(raw_input())
b = int(raw_input())
c = int(raw_input())

perimetro = a + b + c

if abs(b - c) < a < b + c \
   and abs(a - c) < b < a + c \
   and abs(a - b) < c < a + b:
   print 'triangulo valido. %d' % perimetro
   
else: 
	print 'triangulo invalido.'      
