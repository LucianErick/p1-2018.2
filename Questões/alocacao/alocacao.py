#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Alocação MTs

numero = int(raw_input())

if 10 >= numero >= 1:
   sala = 'LCC1-1'
elif 20 >= numero >= 11:
   sala = 'LCC1-2'
elif 30 >= numero >= 21:    
   sala = 'LCC2-1'
elif 40 >= numero >= 31 :
   sala = 'LCC2-2'
else: 
   sala = 'Aluno inexistente.'     

print sala
