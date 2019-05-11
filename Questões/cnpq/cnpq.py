# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação I | 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Bolsa do CNPq

meses = 12
lista_meses = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov', 'dez']
lista_saldos = []
maior_saldo = -500000
dinheiro = 500

for tempo in range(meses):
	
	gasto = int(raw_input())
	
	dinheiro -= gasto
	lista_saldos.append(dinheiro)
	
	dinheiro += 500
 
	if lista_saldos[tempo] > maior_saldo:
		maior_saldo = lista_saldos[tempo]
	
	if lista_saldos[tempo] == maior_saldo:
		maior_mes = lista_meses[tempo]
		
print maior_mes
