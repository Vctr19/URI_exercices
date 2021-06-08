#!/usr/bin/env python3

a = int(input())
b = int(input())

def montar_tabuada(inicio, fim):
    for i in range(inicio, fim+1):
        for j in range (1, 11):
            print(f'{i} x {j} = {i*j}')
        print('-'*10)

if b >= a:
    montar_tabuada(a, b)
else:
    print("Nenhuma tabuada no intervalo!")

