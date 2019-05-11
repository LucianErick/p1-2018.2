#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Ciclo Trigonométrico

numero = float(raw_input())
angulo = numero % 360 

if angulo >= 1 and 89 >= angulo:
     quadrante = 'Quadrante 1'
     print quadrante
elif angulo >= 91 and 179 >= angulo:   
     quadrante = 'Quadrante 2'
     print quadrante
elif angulo >= 181 and 269 >= angulo:
     quadrante = 'Quadrante 3'
     print quadrante
elif angulo >= 271 and 359 >= angulo:
     quadrante = 'Quadrante 4'
     print quadrante
elif angulo == 0 or angulo == 90 or angulo == 180 or angulo == 270 or angulo == 360: 
     quadrante = 'Sobre eixos'
     print quadrante

