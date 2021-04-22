#!/usr/bin/env python3

nota_a = float(input())
nota_b = float(input())
peso_a = 3.5
peso_b = 7.5

m_a = nota_a * peso_a
m_b = nota_b * peso_b
m_c = m_a + m_b

MEDIA = m_c / (peso_a + peso_b)

print(f'MEDIA = {MEDIA:.5f}')
