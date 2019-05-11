#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Mais velho entre duas pessoas

nome_1 = raw_input()
dia_1 = int(raw_input())
mes_1 = int(raw_input())
ano_1 = int(raw_input())
nome_2 = raw_input()
dia_2 = int(raw_input())
mes_2 = int(raw_input())
ano_2 = int(raw_input())

if ano_1 < ano_2 \
   or ano_1 == ano_2 and mes_1 < mes_2 \
   or ano_1 == ano_2 and mes_1 == mes_2 and dia_1 < dia_2:
   print nome_1
   
elif ano_2 < ano_1 \
   or ano_1 == ano_2 and mes_2 < mes_1 \
   or ano_1 == ano_2 and mes_1 == mes_2 and dia_2 < dia_1:
   print nome_2
   
else:
	print 'nenhuma'
