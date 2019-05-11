# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Consumo energia

potencia = int(raw_input())
tempo = int(raw_input()) / 60.0

consumo = (potencia * tempo) / 1000.0

print str(consumo) + ' kWh' 
 
