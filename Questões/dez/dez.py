#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Dez ou soma dez

numero_1 = int(raw_input())
numero_2 = int(raw_input())

if numero_1 == 10 or numero_2 == 10:
   print 'SIM'

elif (numero_1 + numero_2) == 10:
   print 'SIM'
   
else: 
   print 'NAO'
           
