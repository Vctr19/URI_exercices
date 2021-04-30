#!/usr/bin/env python3

dia_semana = str(input())
prazo = int(input())

semana = ('domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado')

def calc_prazo(prazo, dia_compra):

    if prazo == 0:
        res = 'chega hoje!'
    else:
        dia_compra_index = semana.index(dia_compra)
        prazo_index = dia_compra_index + prazo

        if prazo_index >= len(semana):
            dia_entrega = semana[prazo_index - len(semana)]
            res = f'sera entregue {dia_entrega}'
        else:
            res = f'sera entregue {semana[prazo_index]}'

    return res

print(calc_prazo(prazo, dia_semana))

