# coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#UFCG - Programação 1

abstencao = int(raw_input())
a_favor = int(raw_input())
contra = int(raw_input())

total = (abstencao + a_favor + contra)

porcentagem_abstencao = (abstencao * 1.0 / total) * 100
porcentagem_a_favor = (a_favor * 1.0 / total) * 100
porcentagem_contra = (contra * 1.0 / total) * 100
print "Resultado da Votação"
print
print '%i abstenções (%.2f%%)' % (abstencao, porcentagem_abstencao)
print '%i a favor (%.2f%%)' % (a_favor, porcentagem_a_favor)
print '%i contra (%.2f%%)' % (contra, porcentagem_contra)
