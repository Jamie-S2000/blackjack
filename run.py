"""
BlackJack
"""
# Imports
import random

# Global variables
deck = []


def build_deck():
    """
    Builds a deck of cards
    """
    global deck
    suites = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    for suite in suites:
        for i in range(2, 11):
            deck.append((suite, i))
        deck.append((suite, 'Jack'))
        deck.append((suite, 'Queen'))
        deck.append((suite, 'King'))
        deck.append((suite, 'Ace'))
    return deck


def draw_card():
    """
    Draws a card from the deck
    """
    global deck
    card = random.choice(deck)
    deck.remove(card)
    print(card)
    return card

def deal_user():
    """
    Deal two cards to the user
    """
    card1 = draw_card()
    card2 = draw_card()
    return [card1, card2]
