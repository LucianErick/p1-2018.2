#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Clássico dos maiorais

gols_campinense = int(raw_input()) 
gols_treze = int(raw_input())

if gols_campinense > gols_treze:
   vencedor = 'Campinense'
   print vencedor
elif gols_treze > gols_campinense:
	vencedor = 'Treze'
	print vencedor
elif gols_campinense == gols_treze:
	vencedor = 'Empate'
	print vencedor	   
