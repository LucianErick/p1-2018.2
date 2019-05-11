# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Divisão Safra

safra = int(raw_input())
atacado = int(raw_input())
varejo = int(raw_input())

venda_atacado = safra / atacado

resto = safra % atacado

venda_varejo = resto * 1.0 / varejo

print 'Clientes no atacado = %ikg cada.' % venda_atacado
print 'Clientes no varejo = %.2fkg cada.' % venda_varejo
