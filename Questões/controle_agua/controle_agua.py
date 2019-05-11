# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Controle de água

import math

velocidade_de_vazao = float(raw_input())
diametro = float(raw_input())
tempo = float(raw_input())
seccao = (math.pi * diametro ** 2 ) / 4
vazao = velocidade_de_vazao * seccao * 1000            

quantidade_de_agua = tempo * vazao

print "Quantidade de água =", quantidade_de_agua, "litros."
