'''1. Utwórz listę hitsTitles zawierającą tytuły: 'BROTHERS IN ARMS','BOHEMIAN RHAPSODY',
    'STAIRWAY TO HEAVEN','RIDERS ON THE STORM','WISH YOU WERE HERE'''

hit_titles = [
    'BROTHER IN ARMS',
    'BOHEMIAN RHAPSODY',
    'STAIRWAY TO HEAVEN',
    'RIDERS ON THE STORM',
    'WISH YOU WHERE HERE'
    ]

'''2. Dodaj do listy kolejne dwie piosenki: 'CHILD IN TIME' i 'AGAIN'''


hit_titles.extend(['CHILD IN TIME', 'AGAIN'])

print(hit_titles)


'''3. Wygląda na to, że w systemie głosowania była luka.
Na pozycji 3 powinna się znaleźć piosenka 'HOTEL CALIFORNIA' '''

hit_titles.insert(2, 'HOTEL CALIFORNIA')
print(hit_titles)


'''4. Ops... wygląda na to, że system był bardziej zepsuty...
oczywiście to wina IT. Piosenka 'THE SOUND OF SILENCE' powinna znaleźć się na pierwszym miejscu'''

hit_titles.insert(0, 'THE SOUND OF SILENCE')
print(hit_titles)


'''5. To na jakiej pozycji jest teraz 'HOTEL CALIFORNIA'? Odnajdź numer indeksu dla tej piosenki'''

print(hit_titles.index('HOTEL CALIFORNIA'))


'''6. A jednak 'HOTEL CALIFORNIA' powinien zostać usunięty z listy'''

hit_titles.remove('HOTEL CALIFORNIA')
print(hit_titles)


'''7. No i na pierwszym miejscu tytuł "THE SOUND OF SILENCE" powinien zostać zamieniony na "ENJOY THE SILENCE"'''

hit_titles[hit_titles.index('THE SOUND OF SILENCE')] = 'ENJOY THE SILENCE'
print(hit_titles)


'''8. Utwórz kopię listy,
która będzie służyła do odczytania przebojów na antenie. Nowa lista ma nazywać się hitsToRead'''

hits_to_read = hit_titles.copy()
print(hits_to_read)
print()


'''9. Lista do odczytania ma zawierać elementy w odwrotnej kolejności.
Odwróć kolejność elementów na liście hitsToRead.'''

hits_to_read.reverse()
print(hits_to_read)
print()


'''10. A jednak dzisiaj lista przebojów będzie  wyjątkowo prezentowana
w kolejności alfabetycznej. Posortuj hitsToRead w kolejności alfabetycznej'''

hits_to_read.sort()
print(hits_to_read)
print()


'''11. Prowadzący listę przebojów po odczytaniu tytułu usuwa z listy hitsToRead usuwa odczytany element.
Dlatego korzysta z metody pop :). Zasymuluj odczyt dwóch pierwszych pozycji'''

print(hits_to_read.pop(0))
print(hits_to_read.pop(0))
print(hits_to_read)
print()



'''12. W czasie audycji słuchacze domagali się aby zagrać dodatkowo
'NOTHING COMPARES 2 U' i 'WISH YOU WERE HERE'. Utwórz listę additionalSongs zawierającą te dwa tytuły.'''

additional_songs = ['NOTHING COMPARES 2 U', 'WISH YOU WERE HERE']
print(additional_songs)
print()


'''13. Dodaj do listy hitsToRead elementy z listy additionalSongs'''

hits_to_read.extend(additional_songs)
print(hits_to_read)
print()



'''14. Ile razy będzie zagrane 'WISH YOU WERE HERE' a ile razy 'RIDERS ON THE STORM'.
Wyświetl ile razy te piosenki występują na liście hitsToRead.'''

print(f"Wish You Were Here będzie grane {hits_to_read.count('WISH YOU WERE HERE')} razy")
print(f"Riders On The Storm grane {hits_to_read.count('RIDERS ON THE STORM')} razy")
print()


'''15. Audycja się kończy. Wyczyść listę hitsToRead'''

hits_to_read.clear()
print(hits_to_read)




