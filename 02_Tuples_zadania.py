'''1. Utwórz listę o nazwie marketing z elementami:

-loyality program
-client promotion
-market research'''

marketing = ['loyality program', 'client promotion', 'market research']
print(marketing)
print()


'''2. Dodaj do listy element 'public relations'''

marketing.append('public relations')
print(marketing)
print()



'''3. Wyświetl pozycję numer 3'''

print(marketing[2])
print()



'''4. Wstaw na pozycję numer 2 element 'investor relations'''

marketing.insert(1, 'investor relations')
print(marketing)
print()



'''5. Chcesz jednak aby lista znajdowała się w zmiennej o nazwie emailMarketing.
Skopiuj elementy z listy marketing do listy emailMarketing'''


email_marketing = marketing.copy()
print(email_marketing)
print()


'''6. Posortuj listę emailMarketing'''

email_marketing.sort()
print(email_marketing)
print()


'''7. Utwórz nową jednoelementową listę internalEmails. Jedyny element to 'internal communication'''

internal_emails = ['internal communication']
print(internal_emails)
print()



'''8. Dodaj listę internalEmails do listy emailMarketing'''

email_marketing.extend(internal_emails)
print(email_marketing)
print()



'''9. Utwórz tuple, którego wartości pochodzą z listy emailMarketing.
Podczas wyświetlania tuple zwróć uwagę na nawiasy, z jakich skorzystał Python'''

new_tuple = tuple(email_marketing)
print(new_tuple)

