import random


colors = ['Hearts','Diamonds','Clubs','Spades']
figures = ['Ace','King','Queen','Jack','10','9']

all_cards = []
player_1 =  []
player_2 =  []

for color in colors:
    for figure in figures:
        card = figure + " " + color
        all_cards.append(card)

shuffled_cards = [card for card in all_cards]
random.shuffle(shuffled_cards)

for card in shuffled_cards:
    if (shuffled_cards.index(card) + 1) % 2 == 0:
        player_1.append(card)
    else:
        player_2.append(card)

print(player_1)
print()
print(player_2)
