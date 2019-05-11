# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação I | 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Abaixo da Média

nota_total = 0
numero_notas = 0
notas = []

while True:
	
	nota = raw_input()
	
	if nota != 'fim':
	   
	   nota = int(nota)  	
	   notas.append(nota)
	
	elif nota == 'fim':
	
	     break
    
	nota_total += nota
	numero_notas += 1


media = float(nota_total) / numero_notas
print '%.2f' % media

for i in range(0, len(notas)):
	
	if notas[i] < media:
	   	
	   print (i + 1), notas[i]
