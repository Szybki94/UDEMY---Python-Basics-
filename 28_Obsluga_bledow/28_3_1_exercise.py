'''
ZADANIE 1

Zaimportuj moduł os

Przeczytaj od użytkownika informację, którą można zinterpretować jako liczbę,
np. zapytaj o akceptowalną cenę zakupu kolejnego kursu na Udemy. Wynik zapamiętaj w zmiennej line

Przeczytaj od użytkownika ścieżkę do pliku

Bez żadnej dodatkowej kontroli zapisz linię w pliku o wskazanej ścieżce

Przetestuj działanie skryptu podając ścieżkę do pliku który można utworzyć
(np. ścieżka do nieistniejącego pliku w istniejącym katalogu) oraz podając
ścieżkę, której nie można utworzyć (np ścieżka do nieistniejącego pliku
w nieistniejącym katalogu). Zauważ jaki błąd jest wyświetlany w drugim przypadku
'''

import os

line = input('Enter accepted price: ')
filepath =input('Enter filename : ')
 
file = open(filepath,'w+')
file.write(line)
file.close()
