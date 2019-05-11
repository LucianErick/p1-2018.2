#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Fli Flai

primeiro_numero = int(raw_input())
segundo_numero = int(raw_input())
terceiro_numero = int(raw_input())

if (primeiro_numero % 10 == 0) or (segundo_numero % 10 == 0) or (terceiro_numero % 10 == 0):  
   print 'Tumba'	

elif not primeiro_numero % 10 == 0 or not segundo_numero % 10 == 0 or not terceiro_numero % 10 == 0:  
  if primeiro_numero % 2 == 0:
	print 'Fli'

  if segundo_numero % 3 == 0:
	print 'Flai'

  if terceiro_numero % 5 == 0:
	print 'Flu'	



