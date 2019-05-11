# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação I 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Aprovação unidades

unidade = int(raw_input('Unidade? '))
media = float(raw_input('Média de aprovação na unidade?'))

proxima_unidade = unidade + 1
msg = 'O aluno vai para a unidade %d com média %.1f.'
print ' '
print msg % (proxima_unidade, media)
