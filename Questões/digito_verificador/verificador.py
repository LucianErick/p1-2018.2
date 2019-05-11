# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Digito Verificador de 5 dígitos

numero = raw_input()

digitos = int(numero[0]) + int(numero[1]) + int(numero[2]) + int(numero[3]) + int(numero[4])

digito_verificador = digitos % 11

print '%s-%d' % (numero, digito_verificador)
