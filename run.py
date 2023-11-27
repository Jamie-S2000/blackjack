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
aces = []


def build_deck():
    """
    Builds a deck of cards
    """
    suites = ['\u2665', '\u2666', '\u2660', '\u2663']
    for suite in suites:
        for i in range(2, 11):
            deck.append((i, f"the {i} of {suite}"))
        deck.append((10, f"the Jack of {suite}"))
        deck.append((10, f"the Queen of {suite}"))
        deck.append((10, f"the King of {suite}"))
        deck.append(('Ace', f"the Ace of {suite}"))


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
        print("Rules:")
        print("Each player is dealt two cards, the dealer's first card is hidden.")
        print("The aim of the game is to get as close to 21 as possible without going over.")
        print("Face cards are worth 10, Aces are worth 1 or 11 and all other cards are")
        print("worth their face value.")
        print("You may choose to hit (take another card) or stick (keep your hand).")
        print("Once you have chosen to stick the dealer will play.")
        print("The player with the lowest score loses.")
        print("If you go over 21 you lose.")
        print("Good luck!\n")
        input("Press enter to start\n")


def reset_game():
    """
    Reset's the game
    """
    deck.clear()
    hands['user'].clear()
    hands['dealer'].clear()
    aces.clear()
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
        print(f"You were dealt {card_1[1]} and {card_2[1]}\n")
    else:
        print(f"The dealer was dealt {card_1[1]} and a hidden card\n")


def hit(player):
    """
    Hit the player with another card
    """
    card = draw_card()
    hands[player].append(card)
    if player == "user":
        print(f"You were dealt {card[1]}\n")
        print(f"Your hand is now {', '.join(card[1] for card in hands[player])}\n")
    else:
        print("The dealer chose to hit")
        print(f"The dealer was dealt {card[1]}")
        print(f"The dealer's hand is now {', '.join(card[1] for card in hands[player])}\n")


def user_choice():
    """
    Gives user the choice to hit or stick
    """
    choice = input("Would you like to hit or stick? (h/s) \n").lower()
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
    card_values = 0

    for cards in hands[player]:
        if cards[0] == 'Ace':
            if player == 'user':
                ace_value = check_aces()
                card_values += ace_value
            else:
                card_values += 11 if card_values < 11 else 1
        else:
            card_values += cards[0]

    return card_values


def check_aces():
    """
    Checks the hand for aces and stores them each game
    """
    aces_in_hand = []
    for card in hands['user']:
        if card[0] == 'Ace':
            aces_in_hand.append(card)

    for card in aces_in_hand:
        if card[0] == 'Ace' and len(aces) < len(aces_in_hand):
            ace_value = input("You have an ace! Would you like it to be 1 or 11? \n")
            while ace_value not in ['1', '11']:
                ace_value = input("Please choose either 1 or 11: \n")
            aces.append(int(ace_value))
        return sum(aces)


def dealer_choice(user_total):
    """
    Dealer chooses to hit or stick
    """
    card_total = check_hand("dealer")
    while card_total < user_total and card_total < 17 and user_total <= 21:
        hit("dealer")
        card_total = check_hand("dealer")

    if card_total < 21:
        print("The dealer chose to stick\n")

    return card_total


def compare_hands(user_total, dealer_total):
    """
    Compares the totals of the dealers hand and the players hand
    """

    print(f"Your hand is {', '.join(card[1] for card in hands['user'])}\n")
    print(f"The dealer's hand is {', '.join(card[1] for card in hands['dealer'])}\n")
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
    reset_game()
    user_choice()
    user_total = check_hand('user')
    dealer_choice(user_total)
    dealer_total = check_hand('dealer')
    winner = compare_hands(user_total, dealer_total)
    increase_score(winner)


main()
