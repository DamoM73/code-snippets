import random

deck = ["A", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

random.shuffle(deck)

while len(deck) > 0:
    print(deck.pop(0))