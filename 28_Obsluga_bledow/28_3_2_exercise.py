'''
ZADANIE 2

Zmodyfikuj poprzedni przykład tak, że instrukcje wykonujące operacje
na pliku znajdą się w bloku try

Jeżeli dojdzie do błedu wyświetl komunikat "SORRY - WE HAVE AN ERROR"

Wykonaj testy takie jak poprzednio
'''

import os

line = input('Enter accepted price: ')
filepath =input('Enter filename : ')
 
try:
    file = open(filepath,'w+')
    file.write(line)
    file.close()
except:
    print('SORRY WE HAVE AN ERROR. PLEASE TRY AGAIN')
