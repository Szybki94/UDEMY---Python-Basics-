'''1. Utwórz obiekt dictionary o nazwie chanels z następującymi kluczami i wartościami:

-Google - 1480
-Email - 300
-Natural Traffic - 440
-TV Spot - 700'''

chanels = {
    'Google':           1480,
    'Email':            300,
    'Natural Traffic':  440,
    'TV Spot':          700
    }

print(chanels.items())
print()



'''2. Wyświetl wartość skojarzoną z kluczem "Email"'''

print(chanels['Email'])
print()



'''3. Utwórz nowy słownik chanelsUpdate z kluczami i wartościami:

-Natural Traffic -  520
-News - 600'''

chanels_update = {
    'Natural Traffic':      520,
    'News':                 600
    }

print(chanels_update.items())
print()


'''4.Zaktualizuj słownik chanels wartościami z chanelsUpdate'''

chanels.update(chanels_update)
print(chanels.items())
print()



'''5. Wyświetl wszystkie klucze z chanels'''

print(chanels.keys())
print()


'''6. Usuń wartość 'Email' ze słownika'''

chanels.pop('Email')
print(chanels.items())
print()
