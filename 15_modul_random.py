'''1. Zaimportuj moduł random'''

import random

'''2. Wylosuj 10 liczb z zakresu 1-100'''

for num in range(1, 11):
    print(random.randrange(1, 100))

print("------------------------------------------------------------")
print()

'''
3. To nieco dłuższe zadanie:

do zmiennej number1 wylosuj liczbę całkowitą z zakresu 1-100

twoim celem będzie losowanie liczb losowych tak długo, aż znowu wylosujesz liczbę number1. Dodatkowo chcemy policzyć ile prób jest do tego potrzebnych

do zmiennej counter zapisz 1

do zmiennej number2 wylosuj liczbę z zakresu 1-100

wyświetl numer próby (counter) i wylosowaną liczbę (number2)

Tak długo jak długo number1 jest inne niż number2

zwiększ counter o 1

wylosuj ponownie liczbę number2 (liczba całkowita od 1 do 100)

wyświetl numer próby (counter) i wylosowaną liczbę (number2)

Na zakończenie wyświetl podsumowanie z infromacją o ilości prób
'''

number_1 = random.randrange(1, 100)

number_2 = None

counter = 0

while number_1 != number_2:
    counter += 1
    number_2 = random.randrange(1, 100)
    print("Wylosowana liczba:\t%3d \t\t Próba:\t%5d" % (number_2, counter))
print("Szukana liczba:\t\t%3d" % number_1)

print("------------------------------------------------------------")
print()



'''4. Tym razem zbudujesz program losujący skład do rozgrywek "2018 FIFA WORLD CUP RUSSIA".
Utwórz zmienną countries jak poniżej:
'''

countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]


random.shuffle(countries)
group_number = 0

for i in range(len(countries)):
    if i % 4 == 0:
        group_number += 1
        print("========== Group %d ==========" % (group_number))
    print(countries[i])

    


