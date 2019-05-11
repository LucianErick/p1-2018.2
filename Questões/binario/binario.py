# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Conversão de Número na Base 2 para a Base 10

binario = raw_input()
numero_1 = ''
produto = 0
soma = 0
resultado_soma = 0
numero_binario = 0
numero_decimal = 0

for b in binario:
	produto += 1
	numero_1 = b
	b = int(b)
	numero_decimal = b * 2 ** (len(binario) - produto)
	b = 2 ** (len(binario) - produto)
	print numero_1 + ' * ' + str(b) + ' = ' + str(numero_decimal)

for numero_binario in binario:
	soma += 1
	numero_binario = int(numero_binario)
	numero_binario = numero_binario * 2 ** (len(binario) - soma)
	resultado_soma += numero_binario
	 
print binario + '(2)' + ' = ' + str(resultado_soma) + '(10)'	 
