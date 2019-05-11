#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#Universidade Federal de Campina Grande
#Ciência da computação
#Programação 1
#Problema: Tweets

quantidade_de_tweets = float(raw_input('quantidade de tweets? '))
tweets_por_pagina = 400

paginas = quantidade_de_tweets / tweets_por_pagina
percentual_tweets_perdidos = (quantidade_de_tweets % tweets_por_pagina) / quantidade_de_tweets * 100.0

print 'Serão necessárias %d página(s) para visualizar os tweets.' % paginas
print '%.1f%% dos tweets serão perdidos.' % percentual_tweets_perdidos
