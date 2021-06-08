#!/usr/bin/env python3

def obter_notas(qtd_alunos):
    n = []
    c = 0
    while c < qtd_alunos:
        n.append(float(input()))
        c+=1
    return n

def segunda_chance(n):
    n_f = []
    qtd_n_alt = 0

    for i in range(len(n)):
        nova_n = float(input())
        
        if nova_n < 10 or n[i] == 10:
            n_f.append([n[i], '-'])
        else:
            if n[i]+2 > 10:
                n_f.append([10, '*'])
            else:
                n_f.append([n[i]+2, '*'])
            qtd_n_alt += 1

    return n_f, qtd_n_alt


def montar_saida(n_ori, n_fin, qtd_n_alt):
    c=0
    print(f'NOTAS ALTERADAS: {qtd_n_alt}')

    for i in n_fin:
        print(f'{i[1]}({c+1:03}) original: {n_ori[c]:0>5.2f} | final: {i[0]:0>5.2f}')
        c+=1

qtd_alunos = int(input())

notas_originais = obter_notas(qtd_alunos)
notas_finais, qtd_notas_alteradas = segunda_chance(notas_originais)
montar_saida(notas_originais, notas_finais, qtd_notas_alteradas)

