import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = [(rank, suit) for suit in suits for rank in ranks]

random.shuffle(deck)

player1_hand = deck[:5]
player2_hand = deck[5:10]

print("Player 1's hand: ")
for card in player1_hand:
    print(card[0], 'of', card[1])
    
print("\nPlayer 2's hand: ")
for card in player2_hand:
    print(card[0], 'of', card[1])
