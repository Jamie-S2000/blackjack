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
    print(f"You were dealt {user_hand}")


def deal_dealer():
    """
    Deal two cards to the dealer
    """
    dealer_card1 = draw_card()
    dealer_card2 = draw_card()
    dealer_hand.append(dealer_card1)
    dealer_hand.append(dealer_card2)
    print(f"The dealer was delt {dealer_card1} and a hidden card")


def user_hit():
    """
    Hit the user with another card
    """
    hit_card = draw_card()
    user_hand.append(hit_card)
    print(f"You were delt {hit_card}")
    print(f"Your hand is now {user_hand}")

def dealer_hit():
    """
    Hit the dealer with another card
    """
    hit_card = draw_card()
    dealer_hand.append(hit_card)
    print(f"The dealer was delt {hit_card}")
    print(f"The dealer's hand is now {dealer_hand}")


def start_game():
    """
    Starts the game
    """
    input("Welcome to BlackJack! Press enter to start")
    build_deck()
    deal_user()
    deal_dealer()

def user_choice():
    """
    Gives user the choice to hit or stick
    """
    global user_hand
    choice = input("Would you like to hit or stick? (h/s)").lower()
    if choice == 'h':
        print("You chosen to hit")
        user_hit()
        check_hand(user_hand)
    elif choice == 's':
        print("You have chosen to stick")
    else:
        print("Please choose either hit (h) or stick (s)")
        user_choice()


def main():
    start_game()
    
    user_choice()