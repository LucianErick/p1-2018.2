#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Depois do 13

numero_1 = int(raw_input())
numero_2 = int(raw_input())
numero_3 = int(raw_input())

soma = numero_1 + numero_2 + numero_3

if numero_1 != 13 and numero_2 != 13 and numero_3 != 13 and soma != 13:
     print soma
   
elif numero_1 == 13:
     print 0   

elif numero_1 != 13 and numero_2 == 13:
	 print numero_1

elif numero_1 != 13 and numero_2 != 13 and (numero_1 + numero_2) != 13 and numero_3 == 13:
	 print numero_1 + numero_2  
	 
elif numero_1 != 13 and numero_2 != 13 and (numero_1 + numero_2) == 13 and numero_3 == 13:
     print 0
     
elif numero_1 != 13 and numero_2 != 13 and numero_3 != 13 and soma == 13:
	 print 0	 	 	 	    
