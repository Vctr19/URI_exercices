#!/usr/bin/env python3

inicio = int(input())
fim = int(input())
contador = 0

def eh_primo(n):
    cont = 0
    for i in range(1, n+1):
        if n % i == 0:
            cont += 1

    if cont == 2: return True

for i in range(inicio, fim+1):
    if eh_primo(i):
        print(i)
        contador += 1

print(f'primos: {contador}')

