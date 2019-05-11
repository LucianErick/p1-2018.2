#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1 | 2018.2
#Problema: B2 para B10

binario = raw_input()

valor_decimal = 0


for i in range(len(binario) - 1, - 1, - 1):
	
	potencia = 2 ** i
	
	decimal = int(binario[i - 1]) * potencia
	
	print '%s * %d = %d' % (binario[i - 1], potencia, decimal)
	
	if decimal > 0:

		valor_decimal += decimal
	   
print '%s(2) = %d(10)' % (binario, valor_decimal)
