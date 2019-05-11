# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Bolsa do CNPq

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

lista_saldo = []
saldo = 0
maior = 0
num_meses = 0
meses_maiores = []

for i in meses :
    gastos = int(raw_input())    
    saldo += 500
    saldo -= gastos
    lista_saldo.append(saldo)         

for n in lista_saldo:
	if n > maior:
	   maior = n
      
for x in range(len(lista_saldo)):
  num_meses += 1
  if lista_saldo[x] == maior and num_meses == 1:
		print meses[x]
	  
  elif lista_saldo[x] == maior and num_meses >=2:
		
