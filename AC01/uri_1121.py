#!/usr/bin/env python3

preco = float(input())
quantidade = int(input())
desconto_fixo = 10
desconto_por_unidade = 1

def desconto(preco, quantidade):
    preco_total = preco * quantidade
    desc_total = desconto_fixo + desconto_por_unidade * quantidade
    valor_final = preco_total - ((desc_total / 100) * preco_total)
    return valor_final

valor_sem_desconto = preco * quantidade

print(f'{valor_sem_desconto:.2f}')
print(f'{desconto(preco, quantidade):.2f}')

