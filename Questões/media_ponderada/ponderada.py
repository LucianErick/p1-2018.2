# coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#UFCG - Programação 1

nota_1 = float(raw_input())
nota_2 = float(raw_input())
nota_3 = float(raw_input())
peso_1 = float(raw_input())
peso_2 = float(raw_input()) 
peso_3 = 100 - (peso_1 + peso_2)

media = (nota_1 * peso_1 + nota_2 * peso_2 + nota_3 * peso_3) / (peso_1 + peso_2 + peso_3) 

print "Média Final: %.1f" % media
