#!/usr/bin/env python3

carrinho = []

def adicionar(item):
    carrinho.append(item)

def remover(item):
    if item in carrinho:
        carrinho.remove(item)
    else:
        print(f'código {item} não encontrado')

def exibir():
    carrinho.sort(reverse=False)
    print(*carrinho, sep=' ')

while True:
    entrada = input().split(' ')

    if entrada[0] == 'encerrar': exibir() ; break
    elif entrada[0] == 'adicionar': adicionar(int(entrada[1]))
    elif entrada[0] == 'remover': remover(int(entrada[1]))
    elif entrada[0] == 'exibir': exibir()
    elif entrada[0].strip() != '':
        for i in range(len(entrada)):
            carrinho.append(int(entrada[i]))

