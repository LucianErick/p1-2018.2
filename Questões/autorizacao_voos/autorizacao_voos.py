#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1 | 2018.2
#Problema: Autorização Voos

disponivel = int(raw_input())
decolagens = int(raw_input())
decolados = 0

for i in range(decolagens):
	
	necessario = int(raw_input())
	
	if necessario <= disponivel:
	   
	   decolados += 1
	   
	   disponivel -= necessario
	   
print '%d voo(s) autorizados.' % decolados	   	
