'''
ZADANIE 4

Jako ostatnią instrukcję w bloku try dodaj konwersję wartości
zapamiętanej w zmiennej line na typ int. Zapamiętaj wynik w zmiennej value

Wyświetl informację "The value saved in file is...."

Przetestuj program na kilka sposobów: wartość która się
konwertuje na liczbę lub nie, ścieżka, która istnieje lub nie itp.
'''

import os


line = input('Enter accepted price: ')
filepath =input('Enter filename : ')
 
try:
    file = open(filepath,'w+')
    file.write(line)
    value = int(line)
    file.close()
    print('The value saved in file is',value)
except FileNotFoundError as e:
    print('Error opening file',filepath,e)
except:
    print('SORRY WE HAVE AN ERROR. PLEASE TRY AGAIN')
