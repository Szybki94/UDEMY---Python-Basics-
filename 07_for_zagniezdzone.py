'''
ZADANIE 1

W tym zadaniu obliczysz silnię. Silnia  to działanie matematyczne,
które dla liczby n wyznacza wartość mnożąc przez siebie wszystkie
liczby naturalne mniejsze lub równe n. Symbol oznaczający silnię to wykrzyknik, np.:

2! = 1*2 =2
3! = 1*2*3 = 6
4! = 1*2*3*4 = 24
https://pl.wikipedia.org/wiki/Silnia

Zmienna i ma wartość 10. Korzystając z pętli for wyznacz wartość silnia
'''

i=10
n = 1

for j in range(1,i+1):
    n *= j
 
print(i, n)
 
print('------------'*3)



'''
ZADANIE 2

Chcesz wyznaczyć wartości silnia dla liczb od 1 do 10.
Napisz pętlę for iterującą przez wartości od 1 do 10,
a w tej pętli for wyznaczaj silnię dla każdej z tych liczb
'''

x = 10
 
for i in range(1,x+1):
 
    n = 1
    
    for j in range(1,i+1):
        n *= j
 
    print("%2d\t\t%10d" % (i, n))
 
 
print('------------'*3)
