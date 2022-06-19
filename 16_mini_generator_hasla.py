'''
1. Rzuć kostką. Co? Nie masz kostki do gry pod ręką? W takim razie:



Zaimportuj moduł random

Zainicjiuj zmienne min =1 i max = 6

Do zmiennej dice zapisz wynik losowania liczby między min,
a max. W ten sposób zasymulowaliśmy rzut kostką.

Napisz sekwencję poleceń if/elif/else, która w zależności
od wylosowanej wartości wyświetli:

1:
   
 o 
   
 
2:
  o
   
o  
 
3:
  o
 o 
o  
 
4:
o o
   
o o
 
5:
o o
 o 
o o
 
6:
o o
o o
o o

'''

import random

min = 1
max = 6

dice_throw = random.randint(min, max)

if dice_throw == 1:
    print('''
       
     o 

''')
elif dice_throw == 2:
    print('''
      o
       
    o
''')
elif dice_throw == 3:
    print('''
      o
     o 
    o
''')

elif dice_throw == 4:
    print('''
    o o
       
    o o
''')

elif dice_throw == 5:
    print('''
    o o
     o 
    o o
''')

elif dice_throw == 6:
    print('''
    o o
    o o
    o o
''')

print("--------------------------------------------------")
print()

'''
2. Trochę zmieniamy temat. Rzuć pięcioma kostkami:

zadeklaruj zmienną dices jako pustą listę

pięć razy wylosuj liczbę z zakresu min do max i wynik dopisz do listy dices

posortuj listę dices

wyświetl zawartość zmienej dices
'''

dices = []

for num in range(1, 6):
    dices.append(random.randint(min, max))

else:
    dices.sort()
    print(dices)

