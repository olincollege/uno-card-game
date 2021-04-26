class Card:
    
    def __init__(self, clr, rank):
        """
        Args:
            suit: A string representing the suit.
            rank: An int represnting the rank of the card (10-14 is Draw Two, Reverse, Skip and Wild Draw).
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
        pos=0
        possible_card = self.cards[0]
        valid_colors = ["Red", "Blue", "Green", "Yellow"]
        valid_nums = [0,1,2,3,4,5,6,7,8,9]
        #print(str(possible_card).split()[0])
        if str(possible_card).split()[0] in valid_colors and\
            int(str(possible_card).split()[1]) in valid_nums:
            self.middle = self.draw(1)
            print(f"This is the card in the middle {self.middle[0]}")
            return
        while str(possible_card).split()[0] not in valid_colors or\
            int(str(possible_card).split()[1]) not in valid_nums:
            pos+=1
            possible_card = self.cards[pos]
        self.middle = [possible_card]
        self.cards = self.cards[0:pos]+self.cards[pos+1::]

        print(f"This is the card in the middle {self.middle[0]}")
    
    def reshuffle(self):
        new_middle = [self.middle[0]]
        self.cards = self.middle[1::] + self.cards
        self.shuffle()
        self.middle = new_middle
    
    def check_match(self, card):
        type_of_card = str(card).split()
        middle_card = str(self.middle[0]).split()
        if type_of_card[0] == middle_card[0] or \
            type_of_card[1] == middle_card[1]:
            return True
        return False


        


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
            if len(self.hand) == 0:
                raise IndexError
            if card not in self.hand:
                raise ValueError
            if not self.deck.check_match(card):
                raise ValueError
            print("Successful card play")
            print(f"{self.hand}")
            pos = self.hand.index(card)
            if pos < len(self.hand) -1:
                self._hand = self.hand[0:pos] + self.hand[pos+1::]
                print(f"{self.hand}")
            else:
                self._hand = self.hand[0:pos]

            self.deck.middle=[card] + self.deck.middle
            print(f"{self.deck.middle}")
        except (ValueError,IndexError):
            print(f"{card} is not in your hand, your hand is {self.hand}")
            

    
    
class PlayGame:
    """
    iterate through the game
    """
    
    def __init__(self,hand):
        self.hand = hand
           
    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        pass
#        if self.hand > 1:
#            self._player_cycle = Cycle(self.players)
#            self._current_player = next(self._player_cycle)
#        elif self.hand <= 1 and self.hand != 0:
#        else:
#            raise stopIteration
        
        
    