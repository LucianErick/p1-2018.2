#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Ano Bissexto

ano = int(raw_input())

if ano % 400 == 0:
	mensagem = 'é bissexto'
elif (ano % 4 == 0) and not ano % 100 == 0:
    mensagem = 'é bissexto'
else: 
    mensagem = 'não é bissexto'    

print '%i %s' % (ano, mensagem)      	
