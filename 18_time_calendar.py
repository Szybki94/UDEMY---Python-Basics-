import time
 
# sprawdzenie wersji pythona
import sys
print(sys.version)
print("\n" *3)
 
# zamiast
# print(time.clock(), time.localtime(time.clock()))
# korzystaj z funkcji time.perf.counter():
print(time.perf_counter(), time.localtime(time.perf_counter()))
print("\n" *3)

print(time.asctime(time.localtime(time.time())))
print("\n" *3)


import calendar
print(dir(calendar))
print("\n" *3)

calendar.setfirstweekday(6)
print(calendar.calendar(2022))
print("\n" *3)


print("Zadania:")
print('''1. Wyświetl czas (datę i godzinę) w postaci
Unix Epoche (skorzystaj z metody time)\n''')
print(time.time())


print("\n" *3)
print('''2. Wyświetl czas (datę i godzinę) w
postaci czytelnej dla człowieka. W tym celu
złóż metodę localtime z metodą time\n''')
print(time.localtime(time.time()))


print("\n"*3)
print('''3. Każdy z nas ma swoje ważne daty: datę urodzenia swoją,
dziewczyny/chłopaka, dziecka, data przyjęcia do pierwszej pracy,
data zakończenia podstawówki itp. Wyświetl miesiąc zawierający tą datę\n''')
print()
print(calendar.month(1994, 10, w = 10, l = 4))


print("\n"*3)
print('''3. Zmień sposób wyświetlenia daty tak, aby środa była pierwszym dniem tygodnia''')
calendar.setfirstweekday(2)
print("Użyłem komendy:\tcalendar.setfirstweekday(2)")


print("\n"*3)
print('''4. Wyświetl miesiąc z ważną dla Ciebie datą ponownie''')
print()
print(calendar.month(1994, 10, w = 5, l = 2))


print("\n"*3)
print('''5. Sprawdź czy rok 2000 był przestępny''')
print(calendar.isleap(2000))


print("\n"*3)
print('''6. Wyświetl kalendarz za rok 2022 i zobacz
czy układ świąt Bożego Narodzenia wygląda atrakcyjnie
czy nie''')
calendar.setfirstweekday(0)
print(calendar.calendar(2022))
print("Kiepski ten układ T_T")
