# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Conversão de medidas

milhas = float(raw_input())
libras = float(raw_input())
galoes = float(raw_input())

quilometros = milhas * 1.60934
quilogramas = libras * 0.453592
litros = galoes * 3.78541

print str(quilometros), str(quilogramas), str(litros)
