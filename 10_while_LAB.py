'''
ZADANIE 1

Na konto została wpłacona kwota initialCapital w wysokości 20000.
Oprocentowanie na koncie to percent = 0.03. Klient banku postanawia
oszczędzać przez maxTimeYears = 10 lat. Po każdym roku oszczędzania
zarobiona kwota jest dodawana do oszczędności i zarabia odsetki przez
pozostały czas.

Zadeklaruj wymagane zmienne, a następnie stwórz pętlę,
która wyświetli informację o tym ile pieniędzy jest na
koncie pod koniec roku, kiedy odsetki się kapitalizują.
Dodaj na zakończenie informację o całkowitej kwocie
zarobionej w banku.
'''

initial_capital = 20000
extended_capital = 0
percent = 0.03
max_time_years = 10
years=0

while years <= max_time_years:
    extended_capital = initial_capital * (1 + percent)
    earned = initial_capital * percent
    print(f'''
Your initial capital at the
year beginig was:\t\t%6d

At the end of the year
your capital is:\t\t%6d

You earned:\t\t\t%6d''' % (initial_capital, extended_capital, earned ))
    print()
    initial_capital = extended_capital
    years += 1

else:
    total_earned = extended_capital - 20000
    print()
    print("Total earnings:\t\t\t%6d" % total_earned)

print()
print()
'''
ZADANIE 2

Dana jest liczba całkowita dodatnia number = 20730906, Oblicz sumę cyfr tej liczby.
'''

number = 20730906
number_str = str(number)

digit_sum = sum([int(digit) for digit in number_str])
print(f"Digit sum of {number} is:\t{digit_sum}")
