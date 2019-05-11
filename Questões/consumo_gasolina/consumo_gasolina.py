# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Consumo de gasolina

posicao_inicial = float(raw_input())
litros_inicial = float(raw_input())
posicao_final = float(raw_input())
litros_final = float(raw_input())

distancia = posicao_final - posicao_inicial
gasolina_gasta = litros_inicial - litros_final

consumo = distancia / gasolina_gasta

print '%.1f' % consumo

