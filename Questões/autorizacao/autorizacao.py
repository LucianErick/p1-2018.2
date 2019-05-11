# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Autorização voos

tempo_disponivel = int(raw_input())
avioes = int(raw_input())
autorizado = 0

for i in range(avioes):
   tempo_necessario = int(raw_input())
 
   if tempo_necessario < tempo_disponivel:
	   autorizado += 1
	   tempo_disponivel - tempo_necessario 
	   
   if tempo_necessario > tempo_disponivel:
	   autorizado += 0  

print  '%d voo(s) autorizados.' % autorizado
