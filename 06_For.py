'''ZADANIE 1

Dana jest lista:

data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']
Napisz pętlę for, która wyświetli elementy tej listy jeden po drugim.
Podczas wyświetlania elementów konwertuj napisy do wielkich liter.'''

data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']

for d in data:
    print(d.upper())

else:
    print("######################################################")
    print()



'''ZADANIE 2

Jak widzisz, każdy z elementów listy zawiera znak ":".

W pętli for każdy z przetwarzanych napisów rozbij ze względu na ":"
korzystając z funkcji split.

Wynik zapamiętaj w nowej dwuelementowej liście elements.

Następnie wyświetl elements[0] konwertując napis do wielkich liter,
a elements[1] wyświetl bez żadnej konwersji'''

for d in data:
    a = d.split(':')
    print(a)

else:
    print("######################################################")
    print()



'''ZADANIE 3

Rozpocznij od poprzednio utworzonej pętli. Zmieniamy zasady wyświetlania:

Jeżeli w elements[0] znajduje się napis "Error", wyświetl elements[1] konwertując tekst do wielkich liter

w przeciwnym razie wyświetl elements[1] bez żadnej konwersji'''


for d in data:
    a = d.split(':')
    if a[0] == "Error":
        a[1] = a[1].upper()
    print(a)

else:
    print("######################################################")
    print()
