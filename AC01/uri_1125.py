#!/usr/bin/env python3

nota_trabalho = float(input())
nota_prova = float(input())

def media(x, y):
    return (x + y) / 2

def checar_aprovacao(nota1, nota2):
    if media(nota1, nota2) >= 6:
        resultado = 'aprovado'
    elif media(nota1, nota2) < 6 and nota1 >= 2:
        resultado = 'talvez com a sub'
    else:
        resultado = 'reprovado'

    return resultado

print(checar_aprovacao(nota_trabalho, nota_prova))

