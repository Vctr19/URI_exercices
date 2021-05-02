#!/usr/bin/env python3

nome = str(input())
salario_fixo = float(input())
vendas = float(input())
comissao_por_venda = 15

comissao_total = comissao_por_venda / 100 * vendas

print(f'TOTAL = R$ {(salario_fixo + comissao_total):.2f}')

