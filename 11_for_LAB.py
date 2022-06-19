'''
ZADANIE 1

Ciąg Fibonacciego to ciąg rozpoczynający się od 0 i 1
a każda kolejna liczba to suma dwóch poprzednich, np:

0
1
0+1 = 1
1+1 = 2
1+2 = 3
2+3 = 5
....

Korzystając z pętli for napisz program, który wyliczy
fibonacciIterations=20 pierwszych elementów ciągu Fibonacciego
'''

num_list = [0,1]

for num in range(0, 20 - 2):
    iterator = num_list[-2] + num_list[-1]
    num_list.append(iterator)
else:
    print(num_list)

print("-------------------------------------------------")



'''
ZADANIE 2
Masz dany tekst:'''


text = '''Industrial Light & Magic: In this case, you find Python
used in the production process for scripting complex,
computer graphic-intensive films. Originally, Industrial
Light & Magic relied on Unix shell scripting, but it was
found that this solution just couldn’t do the job. Python
was compared to other languages, such as Tcl and Perl, and
chosen because it’s an easier-to-learn language that the
organization can implement incrementally. In addition, Python
can be embedded within a larger software system as a scripting
language, even if the system is written in a language such as
C/C++. It turns out that Python can successfully interact with
these other languages in situations in which some languages can’t.'''

'''Twoim zadaniem jest wyświetlić tylko te słowa, które zawierają literkę "p"'''

words = text.split(" ")
for word in words:
    if word.lower().find('p')>=0:
        print(word)
print("-------------------------------------------------")

'''Należy policzyć ile razy w w/w tekście występowały poszczególne słowa'''

word_dict = {}

for word in words:
    if word not in word_dict:
        word_dict[word] = 1
    elif word in word_dict:
        word_dict[word] += 1

for key, value in word_dict.items():
    print("%s\n%d\n\n" % (key, value))
    
    
