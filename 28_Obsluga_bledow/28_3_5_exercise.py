'''
ZADANIE 5

Dodaj kolejną instrukcję except obsługującą błąd ValueError,
który może być wygenerowany podczas konwersji line na value.

W przypadku tego błędu wyświetl komunikat "The value entered
cannot be converted to a number". Możesz wyświetlić więcej szczegółów o błędzie

Dodaj blok else, w którym będzie wyświetlony komunikat
"Actions completed successfully"

Przetestuj działanie skryptu generując różne błędy
'''

import os


line = input('Enter accepted price: ')
filepath =input('Enter filename : ')
 
try:
    file = open(filepath,'w+')
    file.write(line)
    file.close()
    value = int(line)
    print('The value saved in file is',value)
except FileNotFoundError as e:
    print('Error opening file',filepath,e)
except ValueError as e:
    print('The value entered cannot be converted to a number',line,e)
except:
    print('SORRY WE HAVE AN ERROR. PLEASE TRY AGAIN')
else:
    print('Actions completed successfully')
