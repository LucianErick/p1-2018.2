# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Ataque mais positivo de um campeonato

quant_time = int(raw_input())
times = []
gols = []
maior = 0
n_gol = 0


for i in range(0, quant_time):
	tim = raw_input()
	times.append(tim)
	gol = int(raw_input())
	gols.append(gol)
	n_gol += gol
for n in gols:
	if n > maior:
		maior = n
print'Time(s) com melhor ataque (' + str(maior) + ' gol(s)):'
for x in range(len(gols)):
	if gols[x] == maior:
		print times[x]
		
media = n_gol / (quant_time * 1.0)
print '\n' + 'Média de gols marcados: ' + '%.1f' % media
