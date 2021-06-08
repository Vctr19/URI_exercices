#!/usr/bin/env python3

def receber_registros(n):
    c = 0
    registros = []

    while c < n:
        dado_bruto = input().split(';')
        registros.append(dado_bruto)
        c += 1

    return registros

def montar_saida(ls, b_p, b_n_p):
    print('-'*5)
    print('BÔNUS')
    print('-'*5)

    for i in range(len(ls)):
        nome = ls[i][0]
        inscritos = int(ls[i][1])
        monetizacao = float(ls[i][2])
        premium = ls[i][3]
        bonus_p_ins = b_p if premium == 'sim' else b_n_p
        bonus_final = (inscritos // 1000) * bonus_p_ins
        vlr_total = monetizacao + bonus_final

        print(f'{nome}: R$ {vlr_total:.2f}')

n_canais = int(input())
ls_canais = receber_registros(n_canais)
bonus_premium = float(input())
bonus_n_premium = float(input())
montar_saida(ls_canais, bonus_premium, bonus_n_premium)

