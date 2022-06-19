'''
ZADANIE 1

Zaimportuj moduł math

Przygotuj funkcję GiveGeomSeqElement, która:
-przyjmuje 3 parametry a1 - o domyślnej wartości  2,
która oznacza pierwszy element ciągu, factor - o domyślnej
wartości 2, która oznacza współczynnik ciągu geometrycznego,
index o domyślnej wartości 2, która oznacza  który element
ciągu ma być wyliczony

-dodaj do funkcji komentarz, który opisze co robi ta funkcja
-wylicz wartość ciągu. Odpowiedni wzór znajdziesz

np tu: https://pl.wikipedia.org/wiki/Ci%C4%85g_geometryczny

Wylicz wartość 64 elementu ciągu geometrycznego, którego pierwszym elementem jest 1 a współczynnik wynosi 2
'''

import math

print("ZADANIE 1.")

def give_geom_seq_element(a1=2, factor=2, index=2):

    '''This func is returning sequence element'''

    value = a1*pow(factor,index-1)
    return value

print(give_geom_seq_element(a1=1, factor=2, index=3))
print()

'''
ZADANIE 2

Przetestuj działanie funkcji. Napisz pętlę for,
która wyznaczy i wyświetli elementy a1, a2, a3,...a10
dla ciągu geometrycznego o pierwszym wyrazie równym 3, współczynniku 2
'''
print("ZADANIE 2.")

a1=3
factor=2
maxindex=10

for i in range(1, maxindex):
    an = give_geom_seq_element(a1=a1,factor=factor,index=i)
    print('Iterator ',i,'=%8d'% an)

print()

'''
ZADANIE 3

Przygotuj funkcje GiveFactorForGeomSeq, która wyznaczy
wartość współczynnika gdy znane są 2 kolejne wyrazy ciągu
'''

print("ZADANIE 3.")

def give_factor_for_geom_seq(term, nextterm):
    '''returns factor for geometrical sequence having two following terms of the sequence'''
    return nextterm/term

print(int(give_factor_for_geom_seq(3, 81)))
