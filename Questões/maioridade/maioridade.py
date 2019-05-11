# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação I | 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Maioridade Penal Função
def meu_split(string, breaker):
    nova_string = ''
    nova_lista = []
    string = string + ' '
    for elemento in string:
        if elemento != breaker:
            nova_string += elemento
        else:
            nova_lista.append(nova_string)
            nova_string = ''

    return nova_lista

def maioridade_penal(nomes, idades):

    nomes = meu_split(nomes, ' ')
    idades = meu_split(idades, ' ')
    string = ''
    for i in range(len(idades)):

        if int(idades[i]) >= 18:
            string += nomes[i] + ' '
    resultado = ''
    for e in range(len(string) - 1):
        resultado += string[e]

    return resultado
