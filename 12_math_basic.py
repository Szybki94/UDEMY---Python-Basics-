'''Oto wyniki konkursu Eurowizja 2018 w postaci dwóch list:'''

percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,
           2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,
           3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,
           4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,
           8.740978348,6.174819567]
 
countries = ['Ukraine', 'Spain', 'Slovenia', 'Lithuania', 'Austria', 'Estonia',
             'Norway', 'Portugal','United Kingdom','Serbia','Germany','Albania',
             'France','Czech Republic','Denmark','Australia','Finland','Bulgaria',
             'Moldova','Sweden','Hungary','Israel','Netherlands','Ireland',
             'Cyprus','Italy']

'''Ogólna liczba punktów przyznanych w konkursie to'''

sum_of_points = 4988

'''Wyznacz najniższą i najwyższą wartość z listy percent'''
print(f"Najniższa wartość:\t{min(percent)}")
print(f"Najwyższa wartość:\t{max(percent)}")
print("------------------------------------------------------------------------")
print()

'''Stwórz pętlę for, która wykona się dla zmiennej sterującej i między 0 a (długość listy countries minus 1)

Każdorazowo wyświetl:

odpowiednią wartość z listy percent'''

for i in percent:
    print(i)
else:
    print("------------------------------------------------------------------------")
print()


'''wartość percent "zrzutowaną" na typ int'''

for i in percent:
    print(int(i))
else:
    print("------------------------------------------------------------------------")
print()

'''wartość percent zaokrągloną do dwóch miejsc po przecinku'''
for i in percent:
    print(round(i, 2))
else:
    print("------------------------------------------------------------------------")
print()

'''ilość punktów przyznaną danemu krajowi. Da się to obliczyć,
bo znamy procentową ilość punktów przyznanych danemu krajowi oraz
sumaryczną ilość punktów. Rzutując wynik na int, otrzymasz go w postaci liczby całkowitej
nazwę kraju'''

for row in list(map(list, zip(countries, percent))):
    print(f"{row[0]} posiada punktów: {int(row[1] * sum_of_points / 100)}")
else:
    print("All done :)")

