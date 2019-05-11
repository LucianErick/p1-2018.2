#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#UFCG - Programação 1

peso_a_ser_perdido = float(raw_input())
tempo_exercicio = float(raw_input())
consumo = float(raw_input())

um_kg = 7700
uma_hora_exercicios = 900
gasto_diario = 2000

perda_de_peso_diario = ((tempo_exercicio * uma_hora_exercicios) + gasto_diario) - consumo
objetivo = (peso_a_ser_perdido * um_kg) / perda_de_peso_diario  

print 'Você precisará de %.2f dias de dieta' % objetivo
