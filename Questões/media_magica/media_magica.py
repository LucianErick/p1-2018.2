#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#UFCG - Programação 1 

numero_1 = int(raw_input())
numero_2 = int(raw_input())
numero_3 = int(raw_input())
numero_1_float = (numero_1) * 1.0
numero_2_float = (numero_2) * 1.0
numero_3_float = (numero_3) * 1.0

soma = numero_1_float + numero_2_float + numero_3_float
media_magica = soma / 3

print '%.3f' % media_magica
