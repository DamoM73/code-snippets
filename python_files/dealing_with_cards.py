import random


def create_deck():
    suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
    ranks = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

    deck = []

    for suit in suits:
        for rank in ranks:
            deck.append({"suit":suit, "rank":rank})
            
    return deck


def print_cards(stack):
    for card in stack:
        print(f"{card['rank']} of {card['suit']}")
        
        
def deal_cards(deck, num_hands, cards_per_hand):
    hands = []
    for _ in range(num_hands):
        hands.append([])
    
    for _ in range(cards_per_hand):
        for hand in hands:
            hand.append(deck.pop(0))
            
    return hands
        
    
    
# ---- main loop ----
# make the deck
deck = create_deck()
print_cards(deck)

# shuffle the deck
random.shuffle(deck)
print_cards(deck)

# deal cards
hands = deal_cards(deck,4,5)
for hand in hands:
    print("===============")
    print_cards(hand)
    

