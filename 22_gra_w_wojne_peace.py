import random

colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]

all_cards = []

for f in figures:
    for c in colors:
        f['Color'] = c
        card = f.copy()
        all_cards.append(card)
   

shuffled_cards = all_cards.copy()
random.shuffle(shuffled_cards)

player_1 = []
player_2 = []

for card in shuffled_cards:
    if len(player_1) < 12:
        player_1.append(card)
    else:
        player_2.append(card)

print(player_1)
print(player_2)

while len(player_1) > 0 and len(player_2) > 0:
    player_1_card = player_1.pop(0)
    player_2_card = player_2.pop(0)

    if player_1_card['Power'] == player_2_card['Power']:
        player_1.append(player_1_card)
        player_2.append(player_2_card)
        print("PEACE")
        print("Player_1:%25s%25s%25s" % (player_1_card['Color'], player_1_card['Figure'], player_1_card['Power']))
        print("Player_2:%25s%25s%25s" % (player_2_card['Color'], player_2_card['Figure'], player_2_card['Power']))
        print()
        
    elif player_1_card['Power'] > player_2_card['Power']:
        player_1.append(player_1_card)
        player_1.append(player_2_card)
        print("Player_1 WON")
        print("Player_1:%25s%25s%25s" % (player_1_card['Color'], player_1_card['Figure'], player_1_card['Power']))
        print("Player_2:%25s%25s%25s" % (player_2_card['Color'], player_2_card['Figure'], player_2_card['Power']))
        print()

    elif player_1_card['Power'] < player_2_card['Power']:
        player_2.append(player_1_card)
        player_2.append(player_2_card)
        print("Player_2 WON")
        print("Player_1:%25s%25s%25s" % (player_1_card['Color'], player_1_card['Figure'], player_1_card['Power']))
        print("Player_2:%25s%25s%25s" % (player_2_card['Color'], player_2_card['Figure'], player_2_card['Power']))
        print()
    
