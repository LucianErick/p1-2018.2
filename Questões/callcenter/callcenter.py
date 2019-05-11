#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#UFCG - Proramação 1

segunda = int(raw_input())
terca = int(raw_input())
quarta = int(raw_input())
quinta = int(raw_input())
sexta = int(raw_input())
sabado = int(raw_input())
domingo = int(raw_input())

total = segunda + terca + quarta + quinta + sexta + sabado + domingo
media = (total / 7.0)

print 'Total: %i' % total 
print 'Média: %.2f' % media 
