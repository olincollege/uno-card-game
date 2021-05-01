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
            rank = "Draw Four"
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
        if number_of_cards > len(self.cards):
            self.reshuffle()
        drawn_cards = self.cards[0:number_of_cards]
        self.cards = self.cards[number_of_cards:]
        return drawn_cards
    
    def game_start(self):
        pos=0
        possible_card = self.cards[0]
        invalid_colors = ["Wild"]
        invalid_nums = ["Draw Four", "Card", "Reverse", "Skip", "Draw Two"]
        #print(str(possible_card).split()[0])
        if str(possible_card).split()[0] not in invalid_colors and\
            str(possible_card).split()[1] not in invalid_nums:
            self.middle = self.draw(1)
            print(f"This is the card in the middle {self.middle[0]}")
            return
        while str(possible_card).split()[0] in invalid_colors or\
            str(possible_card).split()[1] in invalid_nums:
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
        #type_of_card = card
        middle_card = self.middle[0]
        if middle_card.clr == card.clr or card.clr == "Wild":
            return True
        elif middle_card.rank == card.rank:
            return True
        return False

        #if type_of_card[0] == middle_card[0] or \
        #    type_of_card[1] == middle_card[1]:
        #    return True
        #return False

    def check_action(self, card):
        if card.rank in range(10,15):
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
            pos = self.hand.index(card)
            if pos < len(self.hand) -1:
                self._hand = self.hand[0:pos] + self.hand[pos+1::]
            else:
                self._hand = self.hand[0:pos]

            self.deck.middle=[card] + self.deck.middle
            return True
        except (ValueError,IndexError):
            print(f"This is not valid move, your hand is {self.hand}")
            print(f"The Card in the middle is: {self.deck.middle[0]}")
            return False

    def draw(self, number_of_cards):
        self._hand += self._deck.draw(number_of_cards)
    
    
class PlayGame:
    """
    iterate through the game
    """

    player_list = []
    
    def __init__(self, deck):
        self.deck = deck
        self.deck.shuffle()
        player_1 = Player(deck)
        player_2 = Player(deck)
        player_3 = Player(deck)
        player_4 = Player(deck)
        self.player_list = [player_1, \
                            player_2, \
                            player_3, \
                            player_4]
        self.order = 1
        self.current_player = 0
    

    def next_player(self):
        next_turn =self.current_player+1*self.order
        if next_turn == -1:
            next_turn = 3
        elif next_turn == 4:
            next_turn = 0
        return next_turn
    
    def draw_card_played(self, number_of_cards):
        self.player_list[self.next_player()].draw(number_of_cards)
        self.skip_card_played()
    
    def reverse_card_played(self):
        self.order = self.order*-1

    def wild_card_played(self):
        color_chosen = input("Choose one of the colors, type as seen ---> Red/Green/Blue/Yellow")
        self.deck.middle[0].clr = color_chosen
    
    def check_for_matches(self, player):
        for card in player._hand:
            if self.deck.check_match(card):
                return True
        player.draw(1)
        print("You had no matches so you take from the deck, here is your new hand")
        print(player._hand)
        return self.check_for_matches(player)
        

    
    def skip_card_played(self):
        self.current_player=self.next_player()

    def check_win(self):
        for player in self.player_list:
            if len(player._hand) == 0:
                return True
        return False
    
    def player_turn(self, player, card_pos):
        try:
            card_pos = int(card_pos) -1
            if card_pos > len(player._hand)-1:
                raise IndexError
            if not player.play_card(player._hand[card_pos]):
                raise ValueError
            if self.deck.check_action(self.deck.middle[0]):
                action = self.deck.middle[0].rank
                if action == "Draw Two":
                    self.draw_card_played(2)
                elif action == "Reverse":
                    self.reverse_card_played()
                elif action == "Skip":
                    self.skip_card_played()
                elif action == "Card":
                    self.wild_card_played()
                elif action == "Draw Four":
                    self.wild_card_played()
                    self.draw_card_played(4)
        except (IndexError, ValueError):
            print("ERROR")
            self.current_player= self.current_player - 1*self.order



    def play(self):
        self.deck.game_start()
        self.current_player = 0
        while not self.check_win():
            print(f"It is {self.current_player+1}'s Turn")
            print(f"This is your hand: {self.player_list[self.current_player]._hand}")
            card_pos = input(f"Player {self.current_player + 1} which card do you want to play type 1 or 2 or ...:")
            self.player_turn(self.player_list[self.current_player], card_pos)
            self.current_player = self.next_player()
            print(f"This is the card in the middle: {self.deck.middle[0]}")


            
            
            







            
#   def __iter__(self):
#        self.n = 0
#        return self
#    
#    def __next__(self):
#        pass
        
    