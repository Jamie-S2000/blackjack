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
            if checkHand('user'):
                break
            choice = input("Would you like to hit or stick? (h/s)").lower()
    elif choice == 's':
        print("You chose to stick")
    else:
        print("Please choose either hit (h) or stick (s)")
        userChoice()

    
def checkHand(player):
    """
    Checks hand to see if it is over 21
    """
    global hands
    if player == 'user':
        cardValuesUser = []
        for cards in hands['user']:
            if cards[0] in ['Jack', 'Queen', 'King']:
                cardValuesUser.append(pictureCardsValues[cards[0]])
            elif cards[0] == 'Ace':
                # ace choice value
                print("You have an ace!")
            else:
                cardValuesUser.append(cards[0])
        if sum(cardValuesUser) > 21:
            print("You are bust!")
            return True
        else:
            return sum(cardValuesUser)
    else:
        cardValuesDealer = []
        for cards in hands['dealer']:
            if cards[0] in ['Jack', 'Queen', 'King']:
                cardValuesDealer.append(pictureCardsValues[cards[0]])
            elif cards[0] in range(2, 11):
                cardValuesDealer.append(cards[0])
            else:
                if sum(cardValuesDealer) + 11 > 21:
                    cardValuesDealer.append(1)
                else:
                    cardValuesDealer.append(11)
        total = sum(cardValuesDealer)
        return total


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


def dealerChoice():
    """
    Dealer chooses to hit or stick
    """
    cardTotal = checkHand('dealer')
    while cardTotal < 17:
        print(f"The dealer chose to hit")
        hit('dealer')
        cardTotal = checkHand('dealer')
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


