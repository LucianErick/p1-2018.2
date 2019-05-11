#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Custo IǸSS

salario = float(raw_input())

#Calculando o INSS a ser pago pelo empregado
if salario <= 1317.07:
    inss_funcionario = salario * 0.08
    
elif 1317.07 < salario <= 2195.12:
    inss_funcionario = salario * 0.09
    
else:
    inss_funcionario = salario * 0.11

#Calculando o INSS a ser pago pelo empregador

inss_empregador = salario * 0.12 

print 'O valor da contribuição do INSS a ser pago pelo empregador é de R$ %.2f' % inss_empregador

print 'O valor da contribuição do INSS a ser pago pelo empregado é de R$ %.2f' % inss_funcionario
