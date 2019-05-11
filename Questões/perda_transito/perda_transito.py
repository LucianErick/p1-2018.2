# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Perda de Tempo no Trânsito

segunda = int(raw_input())
terca = int(raw_input())
quarta = int(raw_input())
quinta = int(raw_input())
sexta = int(raw_input())

tempo_gasto = segunda + terca + quarta + quinta + sexta

media = tempo_gasto / 5

total = 7200

porcentagem = (tempo_gasto * 1.0 / total) * 100

episodios = int(tempo_gasto / 50)

print 'Você perdeu %i min na semana (média de %.1f min por dia).' % (tempo_gasto, media)
print 'Isso significa %.2f%% da sua semana produtiva.' % porcentagem
print 'Daria para assistir %i episódio(s) de House.' % episodios
