'''
ZADANIE 3

Dodaj instrukcję except, która wychwyci błąd FileNotFoundError:

W przypadku tego specyficznego błędu wyświetl komunikat
"Error opening file". Możesz dodać szczegółowe informacje o błędzie
'''

import os

line = input('Enter accepted price: ')
filepath =input('Enter filename : ')
 
try:
    file = open(filepath,'w+')
    file.write(line)
    file.close()
except FileNotFoundError as e:
    print('Error opening file',filepath,e)
except:
    print('SORRY WE HAVE AN ERROR. PLEASE TRY AGAIN')
