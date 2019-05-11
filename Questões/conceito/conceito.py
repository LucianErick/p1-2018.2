#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Conversão de Nota em Conceito

nota_1 = float(raw_input())
nota_2 = float(raw_input())
nota_3 = float(raw_input())
nota_4 = float(raw_input())

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

if 9 <= media:
   print 'Conceito A.'

elif 7.5 <= media < 9:
   print 'Conceito B.'

elif 6 <= media < 7.5:
   print 'Conceito C.'
	   
elif 4 <= media < 6:
   print 'Conceito D.'
	   
elif media < 4:
   print 'Conceito E.'	  	   	      
