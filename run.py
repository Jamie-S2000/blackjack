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
    deck.clear()
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
    return card

def deal_user():
    """
    Deal two cards to the user
    """
    user_card1 = draw_card()
    user_card2 = draw_card()
    print(user_card1, user_card2)
    return [user_card1, user_card2]

def deal_dealer():
    """
    Deal two cards to the dealer
    """
    dealer_card1 = draw_card()
    dealer_card2 = draw_card()
    print(dealer_card1)
    return [dealer_card1, dealer_card2]

def hit():
    """
    Hit the user with another card
    """
    user_card = draw_card()
    print(user_card)
    return user_card