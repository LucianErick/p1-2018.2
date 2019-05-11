# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Ataque Mais Positivo de um Campeonato

numero_de_times = int(raw_input())
lista_nomes = []
lista_gols = []
melhores_times = []
gols_totais = 0.0
mais_gols = 0

for i in range(numero_de_times):
	
	nome = raw_input()
	lista_nomes.append(nome)
	
	gols = int(raw_input())
	lista_gols.append(gols)
    
	gols_totais += gols

# Definindo qual a maior quantidade de gols marcados    
for j in range(len(lista_gols)):
	
	if lista_gols[j] > mais_gols:
	   mais_gols = lista_gols[j]

# Definindo que times marcaram mais gols	   
for k in range(len(lista_gols)):
	
	if lista_gols[k] == mais_gols:
	   melhores_times.append(lista_nomes[k])

media = gols_totais / numero_de_times

print 'Time(s) com melhor ataque (%d gol(s)):' % mais_gols
for l in range(len(melhores_times)):
	print melhores_times[l]
print '\n Média de gols marcados: %.1f' % media	
