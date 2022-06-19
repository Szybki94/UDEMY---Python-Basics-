'''2. Śni Ci się koszmar. Twój nauczyciel matematyki kazał Ci wypisać liczby od 1 do 13
i dla każdej liczby wyliczyć jej kwadrat i sześcian. Ponieważ nauczyciel nie zabronił
używać Pythona, napisz pętlę, która dla liczb od 1 do 13 wyświetli kwadrat
i sześcian tej liczby'''

i = 1

while i <= 13:
    num_1 = i ** 2
    num_2 = i ** 3
    print(f'''
            {i} ^2 = {num_1}
            {i} ^3 = {num_2}
            ''')
    i += 1
else:
    print("Skończyłem")
    print()


'''3. Śni Ci się koszmar. Dziecko kuzynki zafascynowane informatyką
prosi Cię o wymienienie kolejnych potęg dwójki. Postanawiasz znowu skorzystać
z Pythona. Napisz pętlę while, która dla kolejnych liczb całkowitych
x  od 0 do 16 wyznaczy wartość dwa do potęgi x.'''

x = 0

while x <= 16:
    num_1 = 2 ** x
    print(f'''
            2 ^{x} = {num_1}''')
    x += 1
else:
    print("Skończyłem")
    print()



'''1. Dana jest zakodowana informacja w postaci tabeli:

numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

Trzeba odnaleźć takie dwie kolejne liczby, że druga jest kwadratem pierwszej. W tym celu:'''


numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

i = 0

i_max = len(numbers)

while i <= i_max - 2:
    if numbers[i] ** 2 == numbers[i+1]:
        print(i, "Found:\t", numbers[i], numbers[i+1])

    else:
        print(i, "\t\t", numbers[i], numbers[i+1])
        
    i += 1

