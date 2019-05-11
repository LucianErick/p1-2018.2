#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Categorias

nome = raw_input()
idade = int(raw_input())
categoria = ' '

if 5 > idade:
     categoria = 'Não pode competir'
     print '%s, %d anos, %s.' % (nome, idade, categoria)	  
elif 7 >= idade >= 5:
     categoria = 'Infantil A'
     print '%s, %d anos, %s.' % (nome, idade, categoria)
elif 10 >= idade >= 8:
	 categoria = 'Infantil B'
	 print '%s, %d anos, %s.' % (nome, idade, categoria)
elif 13 >= idade >= 11:
	 categoria = 'Juvenil A'
	 print '%s, %d anos, %s.' % (nome, idade, categoria)
elif 17 >= idade >= 14:
     categoria = 'Juvenil B'
     print '%s, %d anos, %s.' % (nome, idade, categoria)
elif idade > 17:    		
	 categoria = 'Senior'
	 print '%s, %d anos, %s.' % (nome, idade, categoria)    	 
