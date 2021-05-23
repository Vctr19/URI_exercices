#!/usr/bin/env python3

n_linhas = int(input())
alfabeto = ('A', 'B', 'C', 'D', 'E', 'F', 'G',
        'H', 'i', 'J', 'K', 'L', 'M', 'N', 'O',
        'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
        'X' 'Y', 'Z')

for i in range(n_linhas):
    print(alfabeto[i] * (i + 1))

