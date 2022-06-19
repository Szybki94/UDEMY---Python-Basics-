'''1.  (*) - proszę wybacz niepoprawną pisownię lajk i share ;)

Pracujesz dla firmy odzieżowej, której celem jest wypromowanie nowej kolekcji ubrań. Firma ogłosiła konkurs,
który ma na celu zdobywanie "lajków" i "udostępnień" na Facebooku. Jeśli strona firmy otrzyma danego dnia
co najmniej 500 "lajków" i co najmniej 100 "udostępnień", to ceny spadną o 10%. Na razie masz napisać fragment
programu, który rozstrzygnie czy warunki promocji są spełnione czy nie. Jeśli już wiesz jak to zrobić "GO ON!", a jeśli chcesz, aby Cię trochę pokierować - zajrzyj do kolejnych punktów:

zadeklaruj zmienną MIN_LIKES  o wartości 500 i MIN_SHARES o wartości 100

zadeklaruj zmienną num_likes i num_shares o wartościach wskazujących na to ile było kliknięć LIKE i SHARE
na Facebooku. Przypisz tym zmiennym wybrane przez Ciebie wartości. Zmieniając te wartości będziesz testować
poprawność swojego programu,np 1300 lajków i 55 sharów

napisz polecenie IF, które w przypadku spełnienia warunku opisanego na początku, wyświetli komunikat o obniżce
ceny, a w przeciwnym razie wyświetli komunikat o braku wystarczającej ilości lajków i sharów

przetestuj działanie polecenia IF zmieniając wartości zmiennych num_like i num_shares



2.  Pracujesz dla restauracji, która chce nagrodzić klientów zamawiających w dni robocze (poza weekendem)
pizze lub duży napój. Klienci spełniający warunki promocji dostaną kupon na darmowego burgera.
Na razie piszesz polecenie decydujące o spełnieniu warunków promocji. Do dyspozycji masz zmienne:

isPizzaOrdered - o wartości True/False, która informuje, czy klient kupił Pizzę

isBigDrinkOrdered - o wartości True/False, która informuje, czy klient zamówił duży napój

isWeekend - o wartości True/False, która informuje, czy jest weekend

Napisz polecenie IF, które w przypadku, gdy klient kupił pizzę lub duży napój w dzień poza weekendem, wyświetli informację o kuponie na Burgera, a w przeciwnym razie wyświetli komunikat zachęcający do dalszych zakupów.

Zmieniaj wejściowe warunki logiczne i testuj, czy polecenie zwraca oczekiwany napis.



3. Twój zespół opracowuje przeglądarkę internetową w Pythonie! Twoim zadaniem jest sprawdzenie,
czy operacja pobierania pliku na dysk ma się szansę udać, czy jest od razu skazana na porażkę ze względu
na brak miejsca na dysku. Na wejściu masz następujące zmienne:

diskSize - zmienna numeryczna (np. o wartości 140) oznaczająca wielkość dysku w GB

diskSizeUsed - zmienna numeryczna (np. o wartości 133) oznaczająca ilość zajętego miejsca na dysku w GB

fileSize - zmienna numeryczna (np o wartości 10) oznaczająca wielkość pobieranego pliku w GB

Zbuduj polecenie IF, które w przypadku, gdy jest wystarczająco wolnego miejsca na dysku wyświetli komunikat
"File can be downloaded". W przypadku, gdy plik jest za duży, ma być wyświetlony komunikat o braku miejsca
na dysku

Zmieniając parametry wejściowe przetestuj działanie polecenia'''


'''Ad 1.'''

MIN_LIKES =     500
MIN_SHARES =    100
a = ""


while a != 'y':
    num_likes = input("Podaj liczbę lajków:\t")
    num_shares = input("Podaj liczbę sharów:\t")

    if int(num_likes) >= MIN_LIKES and int(num_shares) >= MIN_SHARES:
        print("You recived discount!!!")

    else:
        print("You have not enough likes or shares ;(")

    a = input(" Are you done y/n?\t")
    print()


'''Ad 2.'''

b = ""

while b != 'y':

    is_pizza_ordered =          input("Is pizza ordered?[y/n]\t")
    is_big_drink_ordered =      input("Is big drink ordered?[y/n]\t")
    is_weekend =                input("Is weekend?[y/n]\t\t")

    if is_pizza_ordered == 'y':
        is_pizza_ordered = True
    else:
        is_pizza_ordered = False

    if is_big_drink_ordered == 'y':
        is_big_drink_ordered = True
    else:
        is_big_drink_ordered = False

    if is_weekend == 'y':
        is_weekend = True
    else:
        is_weekend = False


    if (is_pizza_ordered or is_big_drink_ordered) and not is_weekend:
        print("Congrats!!! Free burger for You!")
    else:
        print("No burger for You!")

    b = input(" Are you done y/n?\t")



'''Ad 3.'''

diskSize = 140

diskSizeUsed = 133

fileSize = 10



if diskSize - diskSizeUsed >= fileSize :

    print('The file can be downloaded')

else:

    print('There isn\'t enough free disk space to download the file. Sorry :(')
