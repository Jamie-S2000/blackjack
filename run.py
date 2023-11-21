"""
BlackJack
"""

import random

deck = []


def build_deck():
    global deck
    suites = ['H', 'D', 'S', 'C']
    for suite in suites:
        for i in range(2, 11):
            deck.append((suite, i))
        deck.append((suite, 'J'))
        deck.append((suite, 'Q'))
        deck.append((suite, 'K'))
        deck.append((suite, 'A'))
    return deck


