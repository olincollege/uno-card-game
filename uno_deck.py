class Card:
    
    def __init__(self, clr, rank):
        """
        Args:
            suit: A string representing the suit.
            rank: An int represnting the rank of the card (11-13 is J, Q, K).
        """
        self.clr = clr
        self.rank = rank
    
    def __repr__(self):
        #Draw Two = 10, Reverse=11, Skip=12
        #We still have think about the wild and wild draw 4
        #Solution to Question 1 (below) goes here
        if self.rank == 10:
            rank = "Draw Two"
        elif self.rank == 11:
            rank = "Reverse"
        elif self.rank == 12:
            rank = "Skip"
        else:
            rank = self.rank
        #End Solutions
           
        return f"{self.clr} {rank}"

import random

class Deck:
    
    def __init__(self):
        self.cards = []
        for clr in ["Red", "Blue", "Green", "Yellow"]:
            for rank in range(0,13):
                self.cards.append(Card(clr,rank))

    def shuffle(self):
        random.shuffle(self.cards)
        
    def draw(self):
        drawn_card = self.cards[0]
        self.cards = self.cards[1:]
        return drawn_card

