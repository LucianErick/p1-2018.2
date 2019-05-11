#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Peso e IMC

peso = float(raw_input())
altura = float(raw_input())

imc = peso / altura ** 2.0
valor_ideal = 24.9 

peso_final = 24.9 * altura ** 2
variacao_peso = peso_final - peso

print 'IMC atual = %.2f' % imc 
print 'Peso a ser ganho/perdido = %.2f' % variacao_peso

