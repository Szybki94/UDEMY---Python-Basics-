'''1. Zaimportuj moduł math'''

import math

'''
2. Oto wzory pozwalające na wykonanie konwersji stopni na radiany i radianów na stopnie:

1° = (π * rad)/180   
1 rad = 180°/π
'''

'''
3. Zadeklaruj zmienną degree i przypisz jej wartość 360.
Wylicz i wyświetl ile wynosi wartość radianów dla 360 stopni
'''

degree = 360
radian = degree * math.pi /180
print(radian)

'''4. Zmień wartość zmiennej degree na 45 stopni i powtórz obliczenia'''

degree = 45
radian = degree * math.pi /180
print(radian)
print()
print("-------------------------------------")


'''
5. ... ale moduł math ma funkcję radians,
która wykonuje konwersję stopni na radiany!
Porównaj wyniki zwracane przez Twoje obliczenia
z obliczeniami funkcji radians.
'''

print(f'''
360 stopni na radiany to:\t{math.radians(360)},
45 stopni na radiany to:\t{math.radians(45)},''')
print()
print("-------------------------------------")


'''6. Pizzeria oferuje pizze:

small - promień 22 cm, cena, 11.50

big - promień 27 cm, cena 15.60

family - promień 38cm, cena 22.00
'''
small_pizza_r =     22
big_pizza_r =       27
family_pizza_r =    38

small_pizza_prize = 11.5
big_pizza_prize = 15.6
family_pizza_prize =22.0

small_pizza_area =  round(math.pi * small_pizza_r**2 / 1000, 2)
print(str(small_pizza_area) + "m^2")

big_pizza_area =    round(math.pi * big_pizza_r**2 / 1000, 2)
print(str(big_pizza_area) + "m^2")

family_pizza_area = round(math.pi * family_pizza_r**2 / 1000,2)
print(str(family_pizza_area) + "m^2")


small_pizza_prize_sqr = round(small_pizza_prize / small_pizza_area, 2)
print(str(small_pizza_prize_sqr) + "PLN/m^2")

big_pizza_prize_sqr = round(big_pizza_prize / big_pizza_area, 2)
print(str(big_pizza_prize_sqr) + "PLN/m^2")

family_pizza_prize_sqr = round(family_pizza_prize / family_pizza_area, 2)
print(str(family_pizza_prize_sqr) + "PLN/m^2")

print()
print("-------------------------------------")

print(dir(math))

