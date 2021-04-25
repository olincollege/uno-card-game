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
        elif self.rank == 13:
            rank = "Card"
        elif self.rank == 14:
            rank = "Draw 4"
        else:
            rank = self.rank
        #End Solutions
           
        return f"{self.clr} {rank}"

import random

class Deck:

    def __init__(self):
        self.cards = []
        self.middle = []
        for clr in ["Red", "Blue", "Green", "Yellow"]:
            for rank in range(0,13):
                self.cards.append(Card(clr,rank))
                if rank!=0:
                    self.cards.append(Card(clr,rank))
        for _ in range(0,4):
            self.cards.append(Card("Wild", 13))
            self.cards.append(Card("Wild", 13))
            self.cards.append(Card("Wild", 14))


    def shuffle(self):
        random.shuffle(self.cards)
        
    def draw(self, number_of_cards):
        drawn_cards = self.cards[0:number_of_cards]
        self.cards = self.cards[number_of_cards:]
        return drawn_cards
    
    def game_start(self):
        self.middle = self.draw(1)
        print(f"This is the card in the middle {self.middle[0]}")


class Player:


    def __init__(self, Deck):
        self._deck = Deck
        self._hand = self._deck.draw(7)
    
    @property
    def deck(self):
        return self._deck
    
    @property
    def hand(self):
        return self._hand
    
    def play_card(self, card):
        try:
            if card not in self.hand:
                raise ValueError
            print("Successful card play")
            print(f"{self.hand}")
        
        except ValueError:
            print(f"{card} is not in your hand, your hand is {self.hand}")
    


