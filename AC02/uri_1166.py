#!/usr/bin/env python3

divida = int(input())
pag_mensal = int(input())

cont = 1

while divida > 0:
    print(f'pagamento: {cont}')
    print(f'antes = {divida}')

    divida = divida - pag_mensal
    if divida < 0: divida = 0

    print(f'depois = {divida}')
    print('-----')

    cont = cont + 1

