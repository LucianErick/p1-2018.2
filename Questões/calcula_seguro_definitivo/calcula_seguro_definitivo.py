# coding: utf-8
# Universidade Federal de Campina Grande
# Ciência da Computação
# Programação I | 2018.2
# Aluno: Luciano Erick Sousa Figueiredo Filho
# Matrícula: 118110400
# Problema: Cálculo de seguro

def calcula_seguro(valor, respostas):

    pontos = 0
    idade = respostas[0]
    estado_civil = respostas[1]
    portao = respostas[2]
    area_risco = respostas[3]
    moradia = respostas[4]
    condicao_moradia = respostas[5]
    uso_veiculo = respostas[6]
    for i in range(len(respostas)):

        if i == 0:

            if idade <= 21:
                pontos += 20

            elif 22 <= idade <= 30:
                pontos += 15

            elif 31 <= idade <= 40:
                pontos += 12

            elif 41 <= idade <= 60:
                pontos += 10

            elif idade > 60:
                pontos += 20

        elif i == 1:

            if estado_civil == True:
                pontos += 10

            elif estado_civil == False:
                pontos += 20

        elif i == 2:

            if portao == True:
                pontos += 20

            elif portao == False:
                pontos += 10

        if i == 3:

            if area_risco == True:
                pontos += 20

            elif area_risco == False:
                pontos += 10

        elif i == 4:

            if moradia == True:
                pontos += 20

            elif moradia == False:
                pontos += 10

        elif i == 5:

            if condicao_moradia == True:
                pontos += 10

            elif condicao_moradia == False:
                pontos += 20

        elif i == 6:

            if uso_veiculo == 'Lazer':
                pontos += 20

            elif uso_veiculo == 'Misto':
                pontos += 20

            elif uso_veiculo == 'Trabalho':
                pontos += 10

    if pontos <= 80:
        risco = 'Risco Baixo'
        taxa = valor * 0.1

    elif 80 < pontos <= 100:
        risco = 'Risco Medio'
        taxa = valor * 0.2

    elif pontos > 100:
        risco = 'Risco Alto'
        taxa = valor * 0.3

    return [pontos, risco, taxa]
