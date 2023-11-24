"""
BlackJack
"""
import random


deck = []
hands = {
    'user': [],
    'dealer': [],
}
scores = {
    'user': 0,
    'dealer': 0,
}


def build_deck():
    """
    Builds a deck of cards
    """
    suites = ['\u2665', '\u2666', '\u2660', '\u2663']
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
    card = random.choice(deck)
    deck.remove(card)
    return card


def start_game():
    """
    Starts the game
    """
    if not deck:
        print("Welcome to\n")
        print(".------..------..------..------..------..------..------..------..------.")
        print("|B.--. ||L.--. ||A.--. ||C.--. ||K.--. ||J.--. ||A.--. ||C.--. ||K.--. |")
        print("| :(): || :/\: || (\/) || :/\: || :/\: || :(): || (\/) || :/\: || :/\: |")
        print("| ()() || (__) || :\/: || :\/: || :\/: || ()() || :\/: || :\/: || :\/: |")
        print("| '--'B|| '--'L|| '--'A|| '--'C|| '--'K|| '--'J|| '--'A|| '--'C|| '--'K|")
        print("`------'`------'`------'`------'`------'`------'`------'`------'`------'\n")
        input("Press enter to start\n")
    deck.clear()
    hands['user'].clear()
    hands['dealer'].clear()
    build_deck()
    deal("user")
    deal("dealer")


def deal(player):
    """
    Deals two cards to the user and dealer
    """
    card_1 = draw_card()
    card_2 = draw_card()
    hands[player].append(card_1)
    hands[player].append(card_2)
    if player == "user":
        print(f"You were dealt {card_1} and {card_2}\n")
    else:
        print(f"The dealer was dealt {card_1} and a hidden card\n")


def hit(player):
    """
    Hit the player with another card
    """
    card = draw_card()
    hands[player].append(card)
    if player == "user":
        print(f"You were dealt {card}\n")
        print(f"Your hand is now {hands[player]}\n")
    else:
        print("The dealer chose to hit")
        print(f"The dealer was dealt {card}")
        print(f"The dealer's hand is now {hands[player]}\n")


def user_choice():
    """
    Gives user the choice to hit or stick
    """
    choice = input("Would you like to hit or stick? (h/s) ").lower()
    if choice == 'h':
        while choice == 'h':
            print("You chose to hit\n")
            hit("user")
            if check_hand('user') > 21:
                return check_hand('user')
            choice = input("Would you like to hit or stick? (h/s) \n").lower()
    elif choice == 's':
        print("You chose to stick\n")
    else:
        print("Please choose either hit (h) or stick (s) \n")
        user_choice()


def check_hand(player):
    """
    Checks hand to see if it is over 21
    """
    if player == 'user':
        card_values_user = []
        for cards in hands['user']:
            if cards[0] in ['Jack', 'Queen', 'King']:
                card_values_user.append(10)
            elif cards[0] == 'Ace':
                ace_value = check_aces()
                card_values_user.append(ace_value)
            else:
                card_values_user.append(cards[0])

        user_total = sum(card_values_user)
        return user_total

    else:
        card_values_dealer = []
        for cards in hands['dealer']:
            if cards[0] in ['Jack', 'Queen', 'King']:
                card_values_dealer.append(10)
            elif cards[0] in range(2, 11):
                card_values_dealer.append(cards[0])
            else:
                if sum(card_values_dealer) + 11 > 21:
                    card_values_dealer.append(1)
                else:
                    card_values_dealer.append(11)
        dealer_total = sum(card_values_dealer)
        return dealer_total


def check_aces():
    """
    Checks the hand for aces
    """
    ace_value = input("You have an ace! Would you like it to be 1 or 11? \n")
    while ace_value not in ['1', '11']:
        ace_value = input("Please choose either 1 or 11: \n")
    return int(ace_value)


def dealer_choice(user_total):
    """
    Dealer chooses to hit or stick
    """
    card_total = check_hand("dealer")
    if card_total > 21:
        return card_total
    while user_total <= 21 and card_total < 17:
        hit("dealer")
        card_total = check_hand("dealer")

    if card_total < 21:
        print("The dealer chose to stick\n")

    return card_total


def compare_hands(user_total, dealer_total):
    """
    Compares the totals of the dealers hand and the players hand
    """

    print(f"Your hand is {hands['user']}\n")
    print(f"The dealer's hand is {hands['dealer']}\n")
    winner = ""
    if user_total > 21:
        winner = 'dealer'
        print("You went bust!")
    elif dealer_total > 21:
        winner = 'user'
        print("The dealer went bust!")
    elif user_total > dealer_total:
        winner = 'user'
        print("You win!")
    else:
        winner = 'dealer'
        print("The dealer wins!")
    return winner


def increase_score(winner):
    """
    Increases the score of the winner
    """
    if winner == 'user':
        scores['user'] += 1
    else:
        scores['dealer'] += 1

    print("The current scores are: \n")
    print(f"User: {scores['user']}")
    print(f"Dealer: {scores['dealer']}\n")
    play_again()


def play_again():
    """
    Asks the user if they want to play again
    """
    play = input("Would you like to play again? (y/n) \n").lower()
    while play not in ['y', 'n']:
        play = input("Please choose either y or n: \n").lower()
    if play == 'y':
        main()
    elif play == 'n':
        print("Thanks for playing!\n")
        exit()


def main():
    """
    Runs the game
    """
    start_game()
    user_choice()
    user_total = check_hand('user')
    dealer_choice(user_total)
    dealer_total = check_hand('dealer')
    winner = compare_hands(user_total, dealer_total)
    increase_score(winner)


main()
