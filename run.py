"""
BlackJack
"""
# Imports
import random

# Global variables
deck = []
user_hand = []
dealer_hand = []


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
    global user_hand
    user_card1 = draw_card()
    user_card2 = draw_card()
    user_hand.append(user_card1)
    user_hand.append(user_card2)
    print(user_hand)


def deal_dealer():
    """
    Deal two cards to the dealer
    """
    dealer_card1 = draw_card()
    dealer_card2 = draw_card()
    dealer_hand.append(dealer_card1)
    dealer_hand.append(dealer_card2)
    print(dealer_card1)


def user_hit():
    """
    Hit the user with another card
    """
    hit_card = draw_card()
    user_hand.append(hit_card)
    print(hit_card)

def dealer_hit():
    """
    Hit the dealer with another card
    """
    hit_card = draw_card()
    dealer_hand.append(hit_card)
    print(hit_card)