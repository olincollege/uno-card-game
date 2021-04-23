class Card:
    
    def __init__(self, suit, rank):
        """
        Args:
            suit: A string representing the suit.
            rank: An int represnting the rank of the card (11-13 is J, Q, K).
        """
        self.suit = suit
        self.rank = rank
    
    def __repr__(self):
        if self.rank == 1:
            rank = "Ace"
            
        #Solution to Question 1 (below) goes here
        elif self.rank == 11:
            rank = "Jack"
        elif self.rank == 12:
            rank = "Queen"
        elif self.rank == 13:
            rank = "King"
        else:
            rank = self.rank
        #End Solutions
           
        return f"{rank} of {self.suit}"

import random

class Deck:
    
    def __init__(self):
        self.cards = []
        for suit in ["Clubs", "Diamonds", "Hearts", "Spades"]:
            for rank in range(1,14):
                self.cards.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.cards)
        
    def draw(self):
        drawn_card = self.cards[0]
        self.cards = self.cards[1:]
        return drawn_card

