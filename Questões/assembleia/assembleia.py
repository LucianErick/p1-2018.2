#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Assembleia

professores = int(raw_input())
votos_sim = 0
votos_nao = 0
votos_abstencao = 0

for votos in range(professores):
	voto = raw_input()
	if voto == 'sim':
	   votos_sim += 1
	if voto == 'não':	
	   votos_nao += 1
	if voto == 'abstenção':
	   votos_abstencao += 1
	   
if (votos_sim + votos_nao) <= professores / 2:
	print 'Quorum insuficiente.'

elif votos_sim > votos_nao and votos_sim > votos_abstencao:
	print 'Decisão a favor da greve.'
			   		
elif votos_nao > votos_sim and votos_nao > votos_abstencao:
	print 'Decisão contrária à greve.'
				   
elif votos_sim == votos_nao:
    print 'Empate.'			   		
