'''
Tym razem otrzymujesz zadanie zautomatyzowania pobierania danych dotyczących
zamówień kierowanych z aptek do dystrybutora leków. Zamówienia są przesyłane
w postaci plików CSV  i umieszczane w katalogu:

home/kamil/workspace/UDEMY/01_Python_dla_początkujących/27_OS_module/Exercise

Pliki są tam umieszczane przez różne inne procesy w ciągu całego dnia.
Codziennie o godzinie 19:00 będzie uruchamiany skrypt, który przeniesie
te pliki do innego folderu, np c::\temp\yyyy-mm-dd (gdzie yyyy to rok,
mm to miesiąc, a dd to dzień z daty dzisiejszej). Potem na tych plikach
są wykonywane dalsze operacje, jak np. import danych.
'''
import datetime
import os

data_input_catalog = r'/home/kamil/workspace/UDEMY/01_Python_dla_początkujących/27_OS_module/Exercise/input'
data_output_catalog = r'/home/kamil/workspace/UDEMY/01_Python_dla_początkujących/27_OS_module/Exercise/output'

today = datetime.date.today()
today_output_catalog = os.path.join(data_output_catalog, today.strftime("%Y-%m-%d"))

#input folder must exist
is_input_catalog_ok = os.path.isdir(data_input_catalog)

#output folder must exist
is_output_catalog_ok = os.path.isdir(data_output_catalog)

#today output catalog cannot exist
is_today_output_catalog_ok = not(os.path.isdir(today_output_catalog)) and \
                             not(os.path.isfile(today_output_catalog))


if is_input_catalog_ok and is_output_catalog_ok and is_today_output_catalog_ok:
    print('Conditions met! We can continue!')
else:
    print('Prerequisites not met! Check the paths!')

    #display detailed error conditions
    if not is_input_catalog_ok:
        print("Input catalog %s must exist!" % data_input_catalog)
    if not is_output_catalog_ok:
        print("Output catalog %s must exist!" % data_output_catalog)
    if not is_today_output_catalog_ok:
        print("Today's output %s cannot exist (neither as file nor as directory)!" % today_output_catalog)
