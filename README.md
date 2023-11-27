# BlackJack
<br>

## Overview
BlackJack, also known as twenty-one, is a game of chance where players try to make cards add up to, or as close to, 21 as possible. This has been developed to simulate playing in persion on a command line.

The game is played against a dealer (the CPU). The dealer shuffles the deck, deals two cards to each player. Both user cards are revealed and one dealer card is revealed. The player chooses to hit (draw a card) or stick (stick with the cards they have). Then the dealer does the same. In this version, the dealer will only draw cards if their score is below 17. This is similar to real casino rules.
Each hand ends when either one player goes bust (their cards total over 21) or both choose to stick. The total of these cards is then compared and the winner is the closest player to 21. If the totals are the same then the dealer wins.
The game is Python-based and uses dictionaries, for loops, if/elif/else statements and while loops to run.
The game opens with ASCII art in the form of playing cards for the title.
They are shown the rules of the game and then are prompted to play. The game is entirely random with a deck of cards that has cards removed each time they are drawn. After each round a new deck is created and new cards are dealt making sure the deck doesn't run out of cards.
When the user quits the game they are shown the final scores.
[Click here for the final deployment of the game.](https://blackjack-js-d463044b2718.herokuapp.com/)

![Screenshot of "Am I Responsive?" image](/assets/images/am-i-responsive.png)
This shows how the deployed site looks on different devices.
<br>

## Contents
1. [Overview](#overview)
1. [Planning](#planning)
    - [Target Audience](#target-audience)
    - [User Stories](#user-stories)
    - [Site Aims](#site-aims)
    - [Lucid Chart and Other Planning](#lucid-chart-and-other-planning)
    - [Color Scheme and Typography](#color-scheme-and-typography)
1. [Current Features](#current-features)
1. [Future Features and Improvements](#future-features-and-improvements)
1. [Testing](#testing)
    -[Bugs](#bugs)
1. [Deployment](#deployment)
1. [Tech](#tech)
1. [Credits](#credits)
<br>

## Planning

### Target audience
- People looking to play BlackJack.
- People looking to play the game online.
- People who are interested in how Python works.

### User Stories
- As a user, I want to understand the objectives of the game.
- As a user, I want to understand the rules of the game.
- As a user, I want the game to be interactive.
- As a user, I want the game to run well and be bug-free.
- As a user, I want to choose when to finish the game.
- As a user, I want to beat the dealer.

### Site Aims
- To offer a game of BlackJack that is easy to interact with.
- To make the game easy to understand and pick up.
- To provide clear rules of the game and how to win.
- To provide a fun game to the user.

### Lucid Chart and Other Planning
The planning for this project was originally written in a notebook. This was to get a base of how the game would function and the different needs of the game. This was then made into a flowchart to map out how the game would work. This became a massive help in organising the project and getting the game to run smoothly.
Here is the flowchart used:
![Flowchat used in the development of the game](/assets/images/flow-chart.jpeg)

### Color Scheme and Typography
These were not factors in creating this project
<br>

## Current Features

-__Global Variables__
- Deck
    - The deck variable holds all the cards for each round
- Hands
    - The hands variable holds both the dealer's and user's hands.
    - It is made as a dictionary to hold them both together, with the key being the user/dealer, and the value being a list of their cards.
- Scores
    - The scores are also held in a dictionary together.
    - The keys are the user/dealer again and the value is the number of wins.

- __build_deck__
- The deck and deck build function build a 52-card deck of 4 suites with 9 value cards and 4 picture cards.
- Each card is represented as a tuple.
- It is cleared and remade after each round of the game is played.
- It uses Unicode characters for the suites to add some visualisation to the game.

- __draw_card__
- This function takes a card from the deck, removes it from the deck and returns the value of the card.

-__start_game__
This function has two parts to it.
One-half of the function only runs if it is the first time the game has been played. This shows:
- A Title made of playing cards.
- The rules.
- A start game input.
The second half runs each time a round starts:
- It clears the deck, the user's hand and the dealer's hand.
- It rebuilds the deck so it has 52 cards again.
- It runs the deal function for the dealer and user.

-__deal(player)__
This function deals cards to the players.
- It draws two cards from the draw function.
- Adds these to the hands of the current player.
- Prints in the console the user's cards and one of the dealer's cards.

-__hit(player)__
This function is how the player draws more cards.
- It runs the draw function and adds it to their hand.
- It then prints out the new cards and the current hand in the console.

-__user_choice__
This gives the user a choice of hitting or sticking.
- When the user hits, the hit function is run then the hand is checked in the check_hand function
- When the user sticks the user is notified they stuck.

-__check_hand(player)__
This function checks each player's hand
- For both the user and the dealer, all cards bar the aces are put into a list.
- When the user has an Ace, the check_aces function is called.
- When the dealer has an Ace, the value is determined by if the current total is less than 11.
- If the total is less than 11 then the Ace is an 11, otherwise, the Ace is a 1.
- Once the Aces value is chosen the total is determined and returned by the function.

-__check_aces__
-This function allows the user to determine the value of each ace they draw.
- It will not allow any value other than 1 or 11

-__dealer_choice__
This determines whether the dealer should hit or stick.
- The dealer decided depending on if:
    1. The dealer's hand's value is less than the user's.
    2. The dealer hand's value is less than 17.
    3. The user is not bust
- All three of these must be true or the dealer won't hit.
- Once one of these is no longer true the dealer will stick if they aren't bust.
- The total value of the dealer's cards is then returned.

-__compare_hands__
This compares the hands of the dealer and the user.
- Depending on if a player went bust, or whose value was higher, a winner is announced.
- The winner is then returned.

-__increase_score(winner)__
- The winner core is increased
- The scores are printed to the console.
- It then runs the play again function.

-__play_again__
This asks users if they would like to play again
- If they choose "y" then the game runs another round.
- If they choose "n" Then the game prints "thanks for playing" and exits.
<br>

## Future Features and Improvements
There are a few ideas that could help improve and enhance the project.
- A Choice of multiple decks that don't get reset each time could make the game closer to life and more challenging.
- A card counting algorithm for the dealer to make more informed choices making the game more difficult.
- A betting system for the user to wager points against the dealer.
    - This would mean the dealer and user both start with an amount of points that they can win or lose.
- Other rules of the game such as double down and splitting hands.
- Images of each card like the title.
<br>

## Testing
The program was tested to make sure the game functioned correctly throughout development.
- It was tested to make sure the inputs worked.
- It was tested to make sure the code functioned how it should.
- It was tested to make sure the game ended when prompted to.

This was all tested locally in the terminal and on Heroku.

### Bugs
There was one major bug which would stop the game from running:
- Sometimes, when the dealer would hit, they would keep hitting until they drew the whole deck and the game crashed.
- The issue was the dealer's total card value was worked out outside a for loop.
- This caused an issue where the dealer drew a card for each card in the dealer's hand rather than for the total value of the cards in hand.
- It would only happen if the dealer hit and if they were within the stick range it wouldn't happen.
- It meant each draw caused the loop to never reach the last card and so the deck would be drawn and the game would crash.
Here is the bugged and fixed code, it is within the check_hand function:
*Bugged code*:
```
card_values_dealer = []
dealer_total = sum(card_values_dealer)
for cards in hands['dealer']:
    if cards[0] in ['Jack', 'Queen', 'King']:
        card_values_dealer.append(10)
    elif cards[0] in range(2, 11):
        card_values_dealer.append(cards[0])
    else:
        if dealer_total + 11 > 21:
            card_values_dealer.append(1)
        else:
            card_values_dealer.append(11)
return dealer_total
```
*Fixed code*:
```
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
```
This code was refactored (*check_hand(player) function*) so will look different in the final version.

### Validator testing
The code has been run through the [PEP8 python validator](#https://pep8ci.herokuapp.com/).
There are error messages for the title some of the rules being too long but these do not affect the game code.
when it is run on Heroku everything fits in the console without issue and so is fine.
<br>

## Deployment

The project was deployed to Heroku using the following steps:

1. Log into Heroku or create an account.
1. Go to your dashboard.
1. click "New" then "Create new app".
1. Create a unique app name ("blackJack-js" for blackjack plus my initials, not JavaScript), select the correct region and create app.
1. This will direct you to the deploy tab.
1. Navigate to settings.
1. Go to the Config Vars section, click add and add with:
    - KEY = PORT
    - VALUE = 8000
1. Navigate to Buildpacks and add:
    - Heroku/python
    - Heroku/nodejs
**They must be in this order**
1. Once this is done navigate to deploy.
1. Select GitHub as your deployment method.
1. Search for the repository and select it to connect.
1. select the deployment type you would like to use and deploy.
<br>

## Tech
Python was the only technology used in this project.
<br>

### Libraries
**Random** was used to pick the cards.
<br>

### Software
Git and VS Code were used to create and push the code to Github.
Git (Github) was used for version control.
Heroku was used to deploy the project.
Lucid Chart was used to plan the logic
[https://patorjk.com/](https://patorjk.com/) was used for the title.
<br>

## Credits
- [ASCII art generator](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20) for the title.
- Richard Wells, my mentor, who helped to debug the major bug in the project and gave ideas to improve the project.