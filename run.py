"""
BlackJack
"""
# Imports
import random

# Global variables
deck = []
userHand = []
dealerHand = []
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


def dealUser():
    """
    Deal two cards to the user
    """
    global userHand
    userCard1 = drawCard()
    userCard2 = drawCard()
    userHand.append(userCard1)
    userHand.append(userCard2)
    print(f"You were dealt {userHand}")


def dealDealer():
    """
    Deal two cards to the dealer
    """
    dealerCard1 = drawCard()
    dealerCard2 = drawCard()
    dealerHand.append(dealerCard1)
    dealerHand.append(dealerCard2)
    print(f"The dealer was delt {dealerCard1} and a hidden card")


def userHit():
    """
    Hit the user with another card
    """
    hitCard = drawCard()
    userHand.append(hitCard)
    print(f"You were delt {hitCard}")
    print(f"Your hand is now {userHand}")

def dealerHit():
    """
    Hit the dealer with another card
    """
    hitCard = drawCard()
    dealerHand.append(hitCard)
    print(f"The dealer was delt {hitCard}")
    print(f"The dealer's hand is now {dealerHand}")


def startGame():
    """
    Starts the game
    """
    input("Welcome to BlackJack! Press enter to start")
    buildDeck()
    dealUser()
    dealDealer()

def userChoice():
    """
    Gives user the choice to hit or stick
    """
    global userHand
    choice = input("Would you like to hit or stick? (h/s)").lower()
    if choice == 'h':
        while choice == 'h':
            print("You chose to hit")
            userHit()
            if checkHandUser(userHand):
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
    global userHand
    cardValues = []
    for cards in userHand:
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
    global dealerHand
    cardValues = []
    for cards in dealerHand:
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
    cardTotal = checkHandDealer(dealerHand)
    while cardTotal < 17:
        print(f"The dealer chose to hit")
        dealerHit()
        cardTotal = checkHandDealer(dealerHand)
    if cardTotal > 21:
        print("The dealer is bust!")
    else:
        print(f"The dealer chose to stick")
        print(f"The dealer's hand is {dealerHand}")


def main():
    startGame()
    userChoice()
    dealerChoice()

main()


