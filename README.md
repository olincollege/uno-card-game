# uno-card-game
### Raul Frias Perez & Lauren Xiong spring 2021 final project

## Despcription
Uno has been one of the most popular card games across the world because it is entertaining, widespread, and easy to play with friends. Our game Uno has the same rules as the Uno card game to match cards by either number or color. There are also special cards that change the color of the card it is on and cards to give extra cards to other players, these cards are called Action Cards. The goal of the game is to get rid of all the cards in your hand, and the first player who gets rid of all their cards wins the game!

## Rules of the Game
1. Match the card in the middle by either color or number;
2. Watch out for action cards! Plus Two, Skip, Reverse, and Wild Cards;
3. If you are at one card and the game prompts you with: 
"Hit enter once you are finished with your turn"
Please type "Uno!" or else you will get extra cards;
4. Do not look at other player cards!

## Creating the Game
During the implementation of our codes, we created four classes to store the information and iterate through the game in the file named 'uno_deck.py'. To start with, we defined 112 cards in total so that it would be easy to call and use the cards in the rest of the game. Then, we created a class to contain all the cards in the deck. Besides the class of the deck, we created another class which defines and tracks the cards in a player's hand. After that, we iterated through the process of drawing and playing cards, checking for any problems with the player's decision, and moving on to the next player. The game also checks for a winner by seeing if any player has gotten rid of all the cards in theri hand. In the file 'test_uno_deck.py', we implemented unit tests for the game and did troubleshoot to make sure that it functions worked properly.

## Running the Game
To run the code, there is no special packages or libraries needed to download, and there is no changes necessary to the code. All you need to do is to download the repository and run `python uno-game.py` on your terminal. 

## Link to the Website
Click [here](https://rfriasperez.github.io/uno-website/) to access the link to our website
