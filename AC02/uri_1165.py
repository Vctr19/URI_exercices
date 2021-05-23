#!/usr/bin/env python3

acumulador = 0
vic_coin = 0

while True:
    acumulador += vic_coin
    vic_coin = float(input())

    if vic_coin == -1:
        total_vic_coin = acumulador*2.5
        print(f'VC$ {acumulador:.2f}\nR$ {total_vic_coin:.2f}')
        break

