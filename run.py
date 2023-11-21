"""
BlackJack
"""
# Imports
import random

# Global variables
deck = []
user_hand = []
dealer_hand = []
picture_cards_values = {
    'Jack': 10,
    'Queen': 10,
    'King': 10,
}


def build_deck():
    """
    Builds a deck of cards
    """
    global deck
    deck.clear()
    suites = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    for suite in suites:
        for i in range(2, 11):
            deck.append((i, suite))
        deck.append(('Jack', suite))
        deck.append(('Queen', suite))
        deck.append(('King', suite))
        deck.append(('Ace', suite))
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
        while choice == 'h':
            print("You chose to hit")
            user_hit()
            if check_hand_user(user_hand):
                break
            choice = input("Would you like to hit or stick? (h/s)").lower()
    elif choice == 's':
        print("You chose to stick")
    else:
        print("Please choose either hit (h) or stick (s)")
        user_choice()


def check_hand_user(hand):
    """
    Checks the hand to see if it is over 21
    """
    global user_hand
    card_values = []
    for cards in user_hand:
        if cards[0] in ['Jack', 'Queen', 'King']:
            card_values.append(picture_cards_values[cards[0]])
        elif cards[0] == 'Ace':
            # ace choice value
            print("You have an ace!")
        else:
            card_values.append(cards[0])
    if sum(card_values) > 21:
        print("You are bust!")
        return True
    else:
        return False


def check_aces(hand):
    """
    Checks the hand for aces
    """
    card_values = []
    for cards in hand:
        if cards[0] in ["Ace"]:
            ace_value = input("You have an ace! Would you like it to be 1 or 11?")
            return ace_value
        else:
            None


def check_hand_dealer(hand):
    """
    Checks dealer hand value
    """
    global dealer_hand
    card_values = []
    for cards in dealer_hand:
        if cards[0] in ['Jack', 'Queen', 'King']:
            card_values.append(picture_cards_values[cards[0]])
        elif cards[0] == 'Ace':
            if sum(card_values) + 11 > 21:
                card_values.append(1)
                print("The dealer chose for the Ace to equal 1")
            else:
                card_values.append(11)
                print("The dealer chose for the Ace to equal 11")
        else:
            card_values.append(cards[0])
    total = sum(card_values)
    return total


def dealer_choice():
    """
    Dealer chooses to hit or stick
    """
    card_total = check_hand_dealer(dealer_hand)
    while card_total < 17:
        print(f"The dealer chose to hit")
        dealer_hit()
        card_total = check_hand_dealer(dealer_hand)
    if card_total > 21:
        print("The dealer is bust!")
    else:
        print(f"The dealer chose to stick")
        print(f"The dealer's hand is {dealer_hand}")
        compare_hands()


def main():
    start_game()
    user_choice()
    dealer_choice()

main()