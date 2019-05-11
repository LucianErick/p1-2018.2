#coding: utf-8
#Aluno: Luciano Erick Sousa Figueiredo Filho
#Matrícula: 118110400
#UFCG - Programação 1

valor = float(raw_input())
data = str(raw_input())
quantidade_produtos = int(raw_input())
media = valor / quantidade_produtos

print 'Data: ' + str(data)
print 'O valor total da compra foi de R$ %.2f. A média do preço dos produtos é de %.1f.' % (valor, media)
