#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande  
#Ciência da Computação
#Programação 1
#Problema: Operadores

a = int(raw_input())
b = int(raw_input())

adicao = str(a + b) 
subtracao = str(a - b)
multiplicacao = str(a * b)
divisao = str(a / b) 
resto = str(a % b)
exponenciacao = str(a ** b)
negacao_de_a = str(a * -1)
a_igual_b = str(a == b)
a_diferente_b = str(a != b)
a_maior_que_b = str(a > b)
b_maior_que_a = str(b > a)
a_menor_igual_b = str(a <= b)

print '===== Operadores ====='
print 'A = %s' % a
print 'B = %s' % b
print 'Adição = %s' % adicao 
print 'Subtração = %s' % subtracao
print 'Multiplicação = %s' % multiplicacao
print 'Divisão = %s' % divisao
print 'Resto = %s' % resto 
print 'Exponenciação = %s' % exponenciacao
print 'Negação de A = %s' % negacao_de_a
print 'A é igual a B? %s' % a_igual_b
print 'A é diferente de B? %s' % a_diferente_b
print 'A é maior que B? %s' % a_maior_que_b
print 'B é maior que A? %s' % b_maior_que_a
print 'A é menor ou igual a B? %s' % a_menor_igual_b
