#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#UFCG - Programação 1

nome = str(raw_input('Nome? '))
letra = float(raw_input('Letra? R$ '))
orcamento = len(nome) * letra

print 'Orçamento: R$ ' + str(orcamento)
