'''
1. Zadeklaruj zmienną poem (a przy okazji przeczytaj wiersz
i zwróć uwagę na jego znaczenie):
'''

poem = '''1.Runą i w łunach spłoną pożarnych 
Krzyże kościołów, krzyże ofiarne 
I w bezpowrotnym zgubi się szlaku 
W lechickiej ziemi Orzeł Polaków. 
2.O, jasne słońce- wodzu Stalinie! 
Niech sława twoja nigdy nie zginie 
Niechaj jak orły powiedzie z gniazda 
Rosja i z Kremla płonąca gwiazda. 
3.Na ziemskim globie flagi czerwone 
Będą na wiatrach grały jak dzwony 
Czerwona Armia i wódz jej Stalin 
Odwiecznych wrogów na zawsze obali! 
4.Zaćmisz się rychło w czarnej godzinie 
Polsko- Twe córy i syny, 
Wiara i każdy krzyż na mogile, 
U stóp am legą w prochu i pyle! '''

'''
2. Do zmiennej lines zapisz wynik rozbicia
napisu poem ze względu na znak enter czyli "\n".
'''

lines = poem.split("\n")

'''
3. Napisz pętlę for wyświetlającą liniję pierwszą,
dziewiątą, drugą, dziesiątą, trzecią, jedenastą itp.
Pisząc pętlę for pamiętaj o tym że tak na prawdę mówimy  o linijkach 0,8,1,9,2,10...
'''

iterators = [0,8,1,9,2,10]

for i in iterators:
    print(lines[i])
