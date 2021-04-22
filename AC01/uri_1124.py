#!/usr/bin/env python3

natural = int(input())

# func devolte o impar anterior
# e o próximo par de um numero natural
# maior ou igual a 2
def encontrar_par_e_impar(n):

    if (n-1) % 2 == 1:
        impar = n - 1
    else:
        impar = n - 2

    if (n+1) % 2 != 0:
        par = n + 2
    else:
        par = n + 1
    
    print(impar, par)

encontrar_par_e_impar(natural)
