#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Ordena 3 números

numero_1 = int(raw_input())
numero_2 = int(raw_input())
numero_3 = int(raw_input())

if numero_1 <= numero_2 <= numero_3:
   print '%d %d %d' % (numero_1, numero_2, numero_3)
elif numero_1 <= numero_3 <= numero_2:
   print '%d %d %d' % (numero_1, numero_3, numero_2)
elif numero_2 <= numero_1 <= numero_3:
   print '%d %d %d' % (numero_2, numero_1, numero_3)
elif numero_2 <= numero_3 <= numero_1:
   print '%d %d %d' % (numero_2, numero_3, numero_1)  
elif numero_3 <= numero_1 <= numero_2:
   print '%d %d %d' % (numero_3, numero_1, numero_2)
elif numero_3 <= numero_2 <= numero_1:
   print '%d %d %d' % (numero_3, numero_2, numero_1)	        	   
