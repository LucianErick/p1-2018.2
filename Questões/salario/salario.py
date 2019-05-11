#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Salário bruto e líquido

nome = raw_input()
quantidade_horas_extras = float(raw_input()) 
salario_minimo = float(raw_input())
hora_extra = float(raw_input())

salario_hora_extra = quantidade_horas_extras * hora_extra 
salario_bruto = (4.0 * salario_minimo) + salario_hora_extra
inss = 0.12 * salario_bruto
imposto_de_renda = 0.2 * salario_bruto
salario_liquido = salario_bruto - (inss + imposto_de_renda)

print 'O Salário Bruto de %s é de R$ %.2f' % (nome, salario_bruto)
print 'O Salário Líquido de %s é de R$ %.2f' % (nome, salario_liquido)
