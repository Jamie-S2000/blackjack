"""
BlackJack
"""
# Imports
import random

# Global variables
deck = []
hands = {
    'user': [],
    'dealer': [],
}
pictureCardsValues = {
    'Jack': 10,
    'Queen': 10,
    'King': 10,
}


def buildDeck():
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


def drawCard():
    """
    Draws a card from the deck
    """
    global deck
    card = random.choice(deck)
    deck.remove(card)
    return card


def deal(player):
    """
    Deals two cards to the user and dealer
    """
    global hands
    card1 = drawCard()
    card2 = drawCard()
    hands[player].append(card1)
    hands[player].append(card2)
    if player == "user":
        print(f"You were dealt {card1} and {card2}")
    else:
        print(f"The dealer was dealt {card1} and a hidden card")


def hit(player):
    """
    Hit the player with another card
    """
    global hands
    card = drawCard()
    hands[player].append(card)
    if player == "user":
        print(f"You were dealt {card}")
        print(f"Your hand is now {hands[player]}")
    else:
        print(f"The dealer was dealt {card}")
        print(f"The dealer's hand is now {hands[player]}")


def startGame():
    """
    Starts the game
    """
    input("Welcome to BlackJack! Press enter to start")
    buildDeck()
    deal("user")
    deal("dealer")

def userChoice():
    """
    Gives user the choice to hit or stick
    """
    global hands
    choice = input("Would you like to hit or stick? (h/s)").lower()
    if choice == 'h':
        while choice == 'h':
            print("You chose to hit")
            hit("user")
            if checkHandUser(hands['user']):
                break
            choice = input("Would you like to hit or stick? (h/s)").lower()
    elif choice == 's':
        print("You chose to stick")
    else:
        print("Please choose either hit (h) or stick (s)")
        userChoice()


def checkHandUser(hand):
    """
    Checks the hand to see if it is over 21
    """
    global hands
    cardValues = []
    for cards in hands['user']:
        if cards[0] in ['Jack', 'Queen', 'King']:
            cardValues.append(pictureCardsValues[cards[0]])
        elif cards[0] == 'Ace':
            # ace choice value
            print("You have an ace!")
        else:
            cardValues.append(cards[0])
    if sum(cardValues) > 21:
        print("You are bust!")
        return True
    else:
        return False


def checkAces(hand):
    """
    Checks the hand for aces
    """
    cardValues = []
    for cards in hand:
        if cards[0] in ["Ace"]:
            aceValue = input("You have an ace! Would you like it to be 1 or 11?")
            return aceValue
        else:
            None


def checkHandDealer(hand):
    """
    Checks dealer hand value
    """
    global hands
    cardValues = []
    for cards in hands['dealer']:
        if cards[0] in ['Jack', 'Queen', 'King']:
            cardValues.append(pictureCardsValues[cards[0]])
        elif cards[0] in range(2, 11):
            cardValues.append(cards[0])
        else:
            if sum(cardValues) + 11 > 21:
                cardValues.append(1)
            else:
                cardValues.append(11)
    total = sum(cardValues)
    return total


def dealerChoice():
    """
    Dealer chooses to hit or stick
    """
    cardTotal = checkHandDealer(hands['dealer'])
    while cardTotal < 17:
        print(f"The dealer chose to hit")
        hit('dealer')
        cardTotal = checkHandDealer(hands['dealer'])
    if cardTotal > 21:
        print("The dealer is bust!")
    else:
        print(f"The dealer chose to stick")
        print(f"The dealer's hand is {hands['dealer']}")


def main():
    startGame()
    userChoice()
    dealerChoice()

main()


