'''Masz następujące dane wejściowe:'''

inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]

'''
ZADANIE 1.

Załaduj moduł math

Wyświetl informację o ilości elementów w obu listach

Napisz instrukcję if, która:

-jeśli liczba elementów na obu listach jest taka sama,
to rozpocznie przetwarzanie danych, które opiszemy
dalej (na razie wystarczy np wyświetlić napis "ok")

-jeśli liczba elementów nie jest zgodna wyświetli informację
"inputdata and factortable need to have equal number of elements"

Ciąg dalszy skryptu piszesz w pierwszej części polecenia if

Napisz pętlę, która przechodzi przez wszystkie elementy listy input  data

Ciąg dalszy piszesz w tej pętli

wylicz wartość minvalue, która ma wynosić:
<wartość n-tego elementu z inputdata> - <wartość n-tego elementu z factortable>
* <wartość n-tego elementu z inputdata>

oraz wartość maxvalue, która ma wynosić:
<wartość n-tego elementu z inputdata> + <wartość n-tego elementu z factortable>
* <wartość n-tego elementu z inputdata>

Wyświetl wyliczone wartości

Wyznacz liczby
mininteger, która ma być największą liczbą całkowitą mniejszą od minvalue (funkcja floor)
oraz
maxinteger, która ma być najmniejszą liczbą całkowitą większą of maxVALUE (funkcja ceil)

Wyświetl liczby: mininteger, n-ty element listy inputdata i maxinteger

'''

import math

print(f"Długość inputdata:\t{len(inputdata)}")
print(f"Długość factortable:\t{len(factortable)}")

if len(inputdata) == len(factortable):
    for i in inputdata:
        minvalue = i - factortable[inputdata.index(i)] * i
        maxvalue = i + factortable[inputdata.index(i)] * i
        mininteger = math.floor(minvalue)
        maxinteger = math.ceil(maxvalue)
        print(f"minvalue:\t{minvalue}")
        print(f"maxvalue:\t{maxvalue}")
        print(f"miniteger:\t{mininteger}")
        print(f"maxinteger:\t{maxinteger}")
else:
    print("inputdata and factortable need to have equal number of elements")


'''
ZADANIE 2.
Załaduj moduł random

Napisz pętlę, która tak jak poprzednio wyznaczy wartości minvalue
oraz maxvalue, ale tym razem nie chcemy korzystać z danych znajdujących
się w factortable. Zamiast tych wartości wygeneruj liczby losowe z zakresu <0,1>

Wskazówka - możesz rozpocząć od poprzedniego skryptu,
tylko usuń instrukcję if i zamień odwołania do factortable[i] funkcją random.random()
'''

import random

for i in inputdata:
    minvalue = i - random.random() * i
    maxvalue = i + random.random() * i
    mininteger = math.floor(minvalue)
    maxinteger = math.ceil(maxvalue)
    print(f"minvalue:\t{minvalue}")
    print(f"maxvalue:\t{maxvalue}")
    print(f"miniteger:\t{mininteger}")
    print(f"maxinteger:\t{maxinteger}")
    


'''
ZADANIE 3.

Z modułu datetime załaduj typ datetime.

Wyświetl datę dzisiejszą

Wyświetl datę dzisiejszą tak, aby pokazał się tylko rok-miesiac-dzień
'''

from datetime import datetime

print(datetime.now())
print(datetime.now().strftime("%Y-%m-%d"))



















