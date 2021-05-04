class Card:
    """
    This creates a set of 112 cards in total: cards ranged from 0 to 9 for Blue, Green, Red and Yellow each (20 cards per color); 
    8 Draw Two cards, 8 Reverse cards and 8 Skip cards with two cards per color eqch;
    4 Wild cards and 4 Wild Draw Four cards.

    Attributes:
    rank: an integer representing the number on the card
    """
    
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
    """
    This defines and records the cards in the deck that players are going to draw from.
    When cards in the deck are run out, the discarded cards are reshuffled and made into a new deck.

    Attributes:
    number_of_cards: an integer representing the total number of cards left in the deck
    drawn_cards: a list containing the cards drawn to players from the deck
    pos: a number which represents the position of the card in the deck
    possible_card: a method defined in the previous class which represents the cards that might appear in the deck
    invalid_colors: a list containing the colors that are not valid and should be discarded if appearing to be the first of the deck
    invalid_numbers: a list containing the numbers that are not valid and should be discarded if appearing to be the first of the deck
    new_middle: a list representing the cards in the reshuffled deck
    middle_card: a list containing cards in the deck
    """

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

    def check_action(self, card):
        if card.rank in range(10,15):
            return True
        return False


class Player:
    """
    This defines and records the cards in players' hands.

    Attributes:
    _deck: a list representing cards from the deck
    _hand: a list representing cards in a player's hand

    """

    def __init__(self, Deck, name):
        self._deck = Deck
        self._hand = self._deck.draw(7)
        self._name = name

    
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

    def __repr__(self):
        string = ""
        for n in range(0,len(self._hand)):
            string = string + f"Card {n+1}: {self._hand[n]}\n"
        return string
    
    
class PlayGame:
    """
    iterate through the game
    color_chosen: an input arguement which allows players to enter the color of the card they want to play/discard
    valid

    Attributes:
    player_list: a list representing all the players in the game in sequence
    player_1: a list containing the deck of cards on the first player's hand
    player_2: a list containing the deck of cards on the second player's hand
    player_3: a list containing the deck of cards on the third player's hand
    player_4: a list containing the deck of cards on the fourth player's hand
    direction: an int representing which direction the list is being cycled through
    current_player: a integer referring to the order of the current player
    next_turn: an integer which decides the next player after current player's turn
    skip_card_played:
    color_chosen: an input argument which allows the player to enter the next color they want to play after discarding a wild card
    valid_colors: a list containing the colors that are valid might appear in the set of cards
    card_pos: an input arguement which allows the player to enter the position of the card they want to play/discard from the hand
    """

    player_list = []
    
    def __init__(self, deck, player_names):
        self.deck = deck
        self.deck.shuffle()
        player_1 = Player(deck, str(player_names[0]))
        player_2 = Player(deck, str(player_names[1]))
        player_3 = Player(deck, str(player_names[2]))
        player_4 = Player(deck, str(player_names[3]))
        self.player_list = [player_1, \
                            player_2, \
                            player_3, \
                            player_4]
        self.direction = 1
        self.current_player = 0
    

    def next_player(self):
        next_turn =self.current_player+1*self.direction
        if next_turn == -1:
            next_turn = 3
        elif next_turn == 4:
            next_turn = 0
        return next_turn
    
    def draw_card_played(self, number_of_cards):
        self.player_list[self.next_player()].draw(number_of_cards)
        self.skip_card_played()
    
    def reverse_card_played(self):
        self.direction = self.direction*-1

    def wild_card_played(self):
        color_chosen = input("Choose one of the colors, type as seen: Red/Green/Blue/Yellow")
        valid_colors = ["Red","Green", "Blue", "Yellow"]
        if color_chosen in valid_colors:
            self.deck.middle[0].clr = color_chosen
        else:
            print("That is not a valid input please follow the correct format: \"Red\"")
        
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
                if action == 10:
                    self.draw_card_played(2)
                elif action == 11:
                    self.reverse_card_played()
                elif action == 12:
                    self.skip_card_played()
                elif action == 13:
                    self.wild_card_played()
                elif action == 14:
                    self.wild_card_played()
                    self.draw_card_played(4)
        except (IndexError, ValueError):
            print("ERROR")
            self.current_player= self.current_player - 1*self.direction



    def play(self):
        self.deck.game_start()
        self.current_player = 0
        while not self.check_win():
            uno_declare = ""
            print(f"It is {self.current_player+1}'s Turn")
            print(f"This is your hand:\n{self.player_list[self.current_player]}")
            self.check_for_matches(self.player_list[self.current_player])
            card_pos = input(f"{self.player_list[self.current_player]._name} which card do you want to play type 1 or 2 or ...:")
            self.player_turn(self.player_list[self.current_player], card_pos)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            uno_declare = input("Hit enter once you are finished with your turn")
            if len(self.player_list[self.current_player]._hand) == 1 and uno_declare != "Uno":
                self.player_list[self.current_player].draw(2)
                print("You forgot to say Uno :( you have to draw two cards")
            elif len(self.player_list[self.current_player]._hand) == 1 and uno_declare == "Uno":
                print("Uno!")
            self.current_player = self.next_player()
            input(f"Hit Enter once {self.player_list[self.current_player]._name} is at the computer")

            print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\nThis is the card in the middle: {self.deck.middle[0]}")
            


            
            
            