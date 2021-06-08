#!/usr/bin/env python3

lista_tempos = []

while True:
    tempo = int(input())

    if tempo > 0:
        lista_tempos.append(tempo)
    else:
        media = sum(lista_tempos) / len(lista_tempos)
        abaixo_da_media = []

        for i in lista_tempos:
            if i < media: abaixo_da_media.append(i)
        
        print(f'MEDIA: {media:.2f}')
        
        for i in abaixo_da_media:
            print(i)

        break

