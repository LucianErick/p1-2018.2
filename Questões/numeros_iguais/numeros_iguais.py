#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Números iguais

numero_1 = int(raw_input())
numero_2 = int(raw_input())
numero_3 = int(raw_input())

if numero_1 != numero_2 and numero_1 != numero_3 and numero_2 != numero_3:
   print '0'

elif numero_1 == numero_2 and numero_1 == numero_3 and numero_2 == numero_3:
   print '3' 

elif numero_1 == numero_2 or numero_1 == numero_3 or numero_2 == numero_3:
   print '2'
   
     	
