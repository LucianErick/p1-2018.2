#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Aprovados e Reprovados

alunos = int(raw_input())
aprovados = 0
reprovados = 0
nota_apro = 0
nota_repro = 0

for num in range(alunos):
    nota = float(raw_input())
    if nota >= 7.0:
        aprovados += 1
        nota_apro += nota
        
    else:
        reprovados +=1
        nota_repro += nota
        
print 'Reprovados: %d' % reprovados

if reprovados > 0:
    media_repro = nota_repro / reprovados 
    print 'Média: %.1f' % media_repro 
    
print ''
    
print 'Aprovados: %d' % aprovados

if aprovados > 0:
    media_apro = nota_apro / aprovados 
    print 'Média: %.1f' % media_apro
