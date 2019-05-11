#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Caixas em banco

import math
cpf = int(raw_input())

caixa = 1 + int(25 * (cpf * math.pi % 1))

if 1 <= caixa <= 8:
	msg ='térreo'
	print'Caixa %i, '% caixa + msg
	
elif 9 <= caixa <= 20:
	msg = 'primeiro andar'
	print'Caixa %i, '% caixa + msg
	
elif 21 <= caixa <= 25:
    msg ='segundo andar'
    print'Caixa %i, '% caixa + msg
