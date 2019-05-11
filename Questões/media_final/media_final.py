#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#UFCG - Programação 1

nota_parcial = float(raw_input())
nota_final = float(raw_input())
 
media_final = (nota_parcial * 0.6 + nota_final * 0.4) / (0.6 + 0.4) 

print 'Média final: ' + str(media_final) 
