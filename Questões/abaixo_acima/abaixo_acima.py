# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação I
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Abaixo e acima

def organiza_por_media(lista):

    soma = 0
    quantidade = 0

    if len(lista) != 0:

        for valor in lista:
            soma += valor
            quantidade += 1

        media = soma / quantidade

        lista_maiores = []

        for i in range(len(lista) - 1, -1, -1):

            if lista[i] > media:

                lista_maiores.append(lista[i])
                lista.pop(i)

        for j in range(len(lista_maiores) -1, -1, -1):

            lista.append(lista_maiores[j])

    return lista

lista = []
print organiza_por_media(lista)
print lista
