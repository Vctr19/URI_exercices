#!/usr/bin/env python3

inico = int(input())
fim = int(input())

contador = 0

for i in range(inico, fim+1):
    if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
        print(i)
        contador += 1

print(f'bissextos: {contador}')

