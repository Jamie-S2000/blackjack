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
userScore = 0
dealerScore = 0


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
                return True
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
                cardValuesUser.append(10)
            elif cards[0] == 'Ace':
                aceValue = checkAces()
                cardValuesUser.append(aceValue)
            else:
                cardValuesUser.append(cards[0])
        userTotal = sum(cardValuesUser)
        if userTotal > 21:
            print("You are bust!")
            return True
        else:
            return userTotal
    else:
        cardValuesDealer = []
        for cards in hands['dealer']:
            if cards[0] in ['Jack', 'Queen', 'King']:
                cardValuesDealer.append(10)
            elif cards[0] in range(2, 11):
                cardValuesDealer.append(cards[0])
            else:
                if sum(cardValuesDealer) + 11 > 21:
                    cardValuesDealer.append(1)
                else:
                    cardValuesDealer.append(11)
        if sum(cardValuesDealer) > 21:
            print("The dealer is bust!")
            return True
        else:
            return sum(cardValuesDealer)


def checkAces():
    """
    Checks the hand for aces
    """
    
    aceValue = input("You have an ace! Would you like it to be 1 or 11?")
    while aceValue not in ['1', '11']:
        aceValue = input("Please choose either 1 or 11: ")
    return int(aceValue)


def dealerChoice(userTotal):
    """
    Dealer chooses to hit or stick
    """
    cardTotal = checkHand('dealer')
    if userTotal == True:
        return False
    else:    
        while cardTotal < 17:
            print(f"The dealer chose to hit")
            hit('dealer')
            cardTotal = checkHand('dealer')
        if cardTotal > 21:
            print("The dealer is bust!")
            return True
        else:
            print(f"The dealer chose to stick")
            print(f"The dealer's hand is {hands['dealer']}")
            return cardTotal


def compareHands(userTotal, dealerTotal):
    """
    Compares the totals of the dealers hand and the players hand
    """
    winner = ""
    if userTotal == True:
        print("The dealer wins!\n")
        winner = 'dealer'
    elif dealerTotal == True:
        print("You win!\n")
        winner = 'user'
    elif userTotal > dealerTotal:
        print("You win!\n")
        winner = 'user'
    else:
        print("The dealer wins!\n")
        winner = 'dealer'
    
    return winner


def main():
    startGame()
    userChoice()
    dealerChoice()
    userTotal = checkHand('user')
    dealerTotal = checkHand('dealer')
    winner = compareHands(userTotal, dealerTotal)
    
main()