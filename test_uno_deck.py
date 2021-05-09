"""
Check the correctness of functions in icon_averaging
"""
# Import required libraries.
import pytest

# Import the code to be tested.
from uno_deck import (
    Card,
    Deck,
    Player,
    PlayGame
)

# create test objects
test_uno_deck = Deck()
test_uno_deck.game_start()
test_uno_player = Player(test_uno_deck, "name")


@pytest.mark.parametrize("color, rank, resulting_card", [
    # Checks that creating a card with a minimum rank is created correctly
    ("Red", 0, "Red 0"),
    # Checks that creating a card with a maximum rank is created correctly
    ("Green", 9, "Green 9"),
    # Checks that creating a card with rank 10 outputs a Draw Two card
    ("Yellow", 10, "Yellow Draw Two"),
    # Checks that creating a card with rank 11 outputs a Reverse card
    ("Blue", 11, "Blue Reverse"),
    # Checks that creating a card with rank 12 outputs a Skip card
    ("Red", 12, "Red Skip"),
    # Checks that creating a card with rank 13 outputs a Wild Card card
    ("Wild", 13, "Wild Card"),
    # Checks that creating a card with rank 14 outputs a Wild Draw Four card
    ("Wild", 14, "Wild Draw Four"),
])
def test_card(color, rank, resulting_card):
    """
    Checks that the card is created with the appropriate rank and color

    Args:
        color: a string representing the color of the card to be created
        rank: A int representing the rank of the card
    """
    uno_card = Card(color, rank)
    assert str(uno_card) == resulting_card


@pytest.mark.parametrize("resulting_card_count, resulting_middle_count", [
    # Checks that the deck creates 112 cards and starts the middle pile at 0 cards
    (112, 0)
])
def test_deck(resulting_card_count, resulting_middle_count):
    """
    Checks that a deck is being created with all 112 cards and the middle is empty

    Args:
        resulting_card_count: a int representing the total cards in the deck
        resulting_middle_count: a int representing the total cards in the middle
    """
    uno_deck = Deck()
    assert (len(uno_deck.cards), len(uno_deck.middle)) == \
        (resulting_card_count, resulting_middle_count)


def test_shuffle():
    """
    Checks that the shuffle method works properly and the list of cards is randomized
    """
    uno_deck = Deck()
    uno_cards = [] + uno_deck.cards
    uno_deck.shuffle()
    shuffled_uno_cards = [] + uno_deck.cards
    assert uno_cards != shuffled_uno_cards


@pytest.mark.parametrize("number_cards_pulled, resulting_deck_count, resulting_draw_count", [
    # Checks that the draw of 112 cards results in proper values
    (112, 0, 112),
    # Check a draw of 0
    (0, 112, 0),
    # Check a draw of 1
    (1, 111, 1),
    # Check a draw of 4
    (4, 108, 4),
])
def test_deck_draw(number_cards_pulled, resulting_deck_count, resulting_draw_count):
    """
    Checks that the draw method is properly updating the deck and returning the
    correct amount of cards

    Args:
        number_cards_pulled: a int representing the number of calls to draw from the deck
        resulting_deck_count: a int representing the updated count of cards in the deck
        resulting_draw_count: a int representing the number of cards returned from draw
    """
    shuffled_uno_deck = Deck()
    shuffled_uno_deck.shuffle()
    drawn_cards = shuffled_uno_deck.draw(number_cards_pulled)

    assert (len(shuffled_uno_deck.cards), len(drawn_cards)) == \
        (resulting_deck_count, resulting_draw_count)


@pytest.mark.parametrize("card, is_match", [
    # Checks that a card with the same number and color match
    (Card("Red", 0), True),
    # Check that a card with the same color is match
    (Card("Red", 1), True),
    # Checks a card with the same number is a match
    (Card("Blue", 0), True),
    # Checks that an non-matching card returns false
    (Card("Blue", 1), False),
    # Checks that a action card of the same color is a match
    (Card("Red", 10), True),
    # Checks that a action card of different color is not a match
    (Card("Blue", 10), False),
    # Checks that a Wild Card is a match
    (Card("Wild", 13), True),
    # Checks that a Wild Draw Four is match
    (Card("Wild", 14), True),
])
def test_deck_check_match(card, is_match):
    """
    Checks that the average image finder returns an average of all the images in the list
    using our second color averaging method.

    Args:
        image_list: a list representing the images to average.
        resulting_image: a image representing the expected resulting average image.
    """
    uno_deck = Deck()
    uno_deck.game_start()

    assert uno_deck.check_match(card) == is_match


@pytest.mark.parametrize("card, is_action", [
    # Checks a normal card returns false
    (Card("Red", 0), False),
    # Checks that a normal card of a different color returns false
    (Card("Blue", 1), False),
    # Check a Yellow Draw Two results in True
    (Card("Yellow", 10), True),
    # Check a Green Reverse results in True
    (Card("Green", 11), True),
    # Check a Red Skip results in True
    (Card("Red", 12), True),
    # Check a Wild Card results in True
    (Card("Wild", 13), True),
    # Check a Wild Draw Four results in True
    (Card("Wild", 14), True),
])
def test_deck_check_action(card, is_action):
    """
    Checks that when given an action card check_action results in true otherwise false

    Args:
        card: a card to be checked
        is_action: a boolean representing the expected result of check_action
    """
    uno_deck = Deck()
    assert uno_deck.check_action(card) == is_action


@pytest.mark.parametrize("player_name, returned_name", [
    # Check a name that is a composed of a number
    ("1", "1"),
    # Checks a name composed of no numbers
    ("Name", "Name"),
    # Check a name composed of numbers and letters
    ("Name1", "Name1"),
    # Check a empty name
    ("", ""),
])
def test_player_display_name(player_name, returned_name):
    """
    Checks that display_name returns the proper player name

    Args:
        player_name: a string representing the player name
        returned_name: a string representing the expected outcome
    """
    uno_deck = Deck()
    uno_player = Player(uno_deck, player_name)
    assert uno_player.display_name() == returned_name


@pytest.mark.parametrize("number_cards_pulled, number_cards_in_hand", [
    # Checks that a draw of 2 results in 9 cards in hand
    (2, 9),
    # Checks that a draw of 0 results in 7 cards in hand
    (0, 7),
    # Checks that a draw of 4 results in 11 cards in hand
    (4, 11),
    # Checks that a draw of 1 results in 8 cards in hand
    (1, 8),
    # Checks that a draw of 13 results in 20 cards in hand
    (13, 20),
])
def test_player_draw(number_cards_pulled, number_cards_in_hand):
    """
    Checks that the draw method in player correctly updates the player's hand

    Args:
        number_cards_pulled: a int representing the number of cards to draw
        number_cards_in_hands: a int representing the resulting number of cards in the
            players hand
    """
    uno_deck = Deck()
    uno_player = Player(uno_deck, "name")
    uno_player.draw(number_cards_pulled)
    assert len(uno_player.hand) == number_cards_in_hand


@pytest.mark.parametrize("card, resulting_hand_size, middle_size, successful_move", [
    # Check that playing a Red 1 Card into a middle deck of Red 0 updates the game
    (test_uno_player.hand[2], 6, 2, True),
])
def test_player_play_card(card, resulting_hand_size, middle_size, successful_move):
    """
    Checks that play_card properly updates the game

    Args:
        card: a card from the player hand to be played
        resulting_hand_size: a int representing the len of the updated player hand
        middle_size: a int representing the updated card count of the middle
        successful_move: a boolean representing if it was a successful move
    """

    assert (test_uno_player.play_card(card), len(test_uno_player.hand), len(test_uno_deck.middle)) \
        == (successful_move, resulting_hand_size, middle_size)


@pytest.mark.parametrize("set_direction, set_current_player, next_player", [
    # Check the next player after the player in position 0 going forward
    (1, 0, 1),
    # Check the next player after the player in position 0 going in reverse
    (-1, 0, 3),
    # Check the next player after the player in position 3 going forward
    (1, 3, 0),
    # Check the next player after the player in position 3 going in reverse
    (-1, 3, 2),
])
def test_next_player(set_direction, set_current_player, next_player):
    """
    Checks that next_player returns the correct next player to play

    Args:
        set_direction: a int representing the direction 1 for forward and -1 for reverse
        set_current_player: a int representing the current player
        next_player: a int representing the expected next_player
    """
    uno_deck = Deck()
    uno_game = PlayGame(uno_deck, ["0", "1", "2", "3"])
    uno_game.direction = set_direction
    uno_game.current_player = set_current_player

    assert uno_game.next_player() == next_player


@pytest.mark.parametrize("set_direction, set_current_player, number_of_cards,\
    card_count_next_player, next_player", [
    # Checks that player 0 playing a 4 draw card updates the game correctly
    (1, 0, 4, 11, 2),
    # Checks that player 0 playing a 2 draw card updates the game correctly
    (1, 0, 2, 9, 2),
    # Checks that player 0 playing a 2 draw card updates the game correctly
    (1, 1, 2, 9, 3),
    # Checks that player 0 playing a 2 draw card updates the game correctly
    (1, 2, 2, 9, 0),
    # Checks that player 0 playing a 4 draw card updates the game correctly in reverse
    (-1, 0, 4, 11, 2),
    # Checks that player 0 playing a 2 draw card updates the game correctly in reverse
    (-1, 0, 2, 9, 2),
    # Checks that player 0 playing a 2 draw card updates the game correctly in reverse
    (-1, 1, 2, 9, 3),
    # Checks that player 0 playing a 2 draw card updates the game correctly in reverse
    (-1, 2, 2, 9, 0),
])
def test_draw_card_played(set_direction, set_current_player, number_of_cards,
                          card_count_next_player, next_player):
    """
    Checks that a player playing a draw card updates the game correctly by giving the proper count
    of cards to the next player and skipping them

    Args:
        set_direction: a int representing the direction 1 for forward and -1 for reverse
        set_current_player: a int representing the current player
        number_of_cards: a int representing the number of cards the next player must draw
        card_count_next_player: a int representing the expected amount of cards the next player
            must hold afterwards
        next_player: a int representing the expected next_player
    """
    uno_deck = Deck()
    uno_game = PlayGame(uno_deck, ["0", "1", "2", "3"])
    uno_game.direction = set_direction
    uno_game.current_player = set_current_player
    uno_game.draw_card_played(number_of_cards)
    cards_next_player = len(
        uno_game.player_list[set_current_player+set_direction].hand)
    new_player = uno_game.next_player()

    assert (cards_next_player, new_player) == (
        card_count_next_player, next_player)


@pytest.mark.parametrize("set_direction, new_direction", [
    # Checks that a forward direction results in the reverse direction after a reverse card played
    (1, -1),
    # Checks that reverse direction results in the forward direction after a reverse card played
    (-1, 1),
])
def test_reverse_played(set_direction, new_direction):
    """
    Checks that the reverse_played method properly changes the direction

    Args:
        set_direction: a int representing the current direction of the game
        new_direction: a int representing the expected new direction of the game
    """
    uno_deck = Deck()
    uno_game = PlayGame(uno_deck, ["0", "1", "2", "3"])
    uno_game.direction = set_direction
    uno_game.reverse_card_played()

    assert uno_game.direction == new_direction


@pytest.mark.parametrize("middle_card, set_player_hand, set_card_deck, resulting_player_hand_len", [
    # Check having a match already in hand
    ([Card("Red", 1)], [Card("Red", 0)], [Card("Blue", 2), Card("Yellow", 3)], 1),
    # Check with the first card in the deck matching by color
    ([Card("Blue", 1)], [Card("Red", 0)], [
     Card("Blue", 2), Card("Yellow", 3)], 2),
    # Check with the first card in the deck matching by color
    ([Card("Green", 2)], [Card("Red", 0)], [
     Card("Blue", 2), Card("Yellow", 3)], 2),
    # Check with the second card in the deck matching by color
    ([Card("Yellow", 1)], [Card("Red", 0)], [
     Card("Blue", 2), Card("Yellow", 3)], 3),
    # Check with the second card in the deck matching by number
    ([Card("Green", 3)], [Card("Red", 0)], [
     Card("Blue", 2), Card("Yellow", 3)], 3),
])
def test_playgame_check_for_matches(middle_card, set_player_hand, set_card_deck,
                                    resulting_player_hand_len):
    """
    Checks that the check matches pulls from the deck until a match is found if
    there no match in the hand already

    Args:
        middle_card: a list representing the current middle card
        set_player_hand: a list representing the current player hand
        set_card_deck: a list representing the current cards in the deck
        resulting_player_hand_len: a int representing the updated length of the player hand
    """
    uno_deck = Deck()
    uno_deck.middle = middle_card
    uno_game = PlayGame(uno_deck, ["0", "1", "2", "3"])
    uno_deck.cards = set_card_deck
    uno_game.player_list[0]._hand = set_player_hand
    uno_game.check_for_matches(uno_game.player_list[0])
    length_of_hand = len(uno_game.player_list[0].hand)

    assert length_of_hand == resulting_player_hand_len


@pytest.mark.parametrize("set_direction, set_current_player, next_player", [
    # Check the next player after the player in position 0 plays a skip card going forward
    (1, 0, 2),
    # Check the next player after the player in position 0 plays a skip card going in reverse
    (-1, 0, 2),
    # Check the next player after the player in position 3 plays a skip card going forward
    (1, 3, 1),
    # Check the next player after the player in position 3 plays a skip card going in reverse
    (-1, 3, 1),
])
def test_playgame_skip_card_played(set_direction, set_current_player, next_player):
    """
    Checks that next_player returns the correct next player to play after a
    skip card is played

    Args:
        set_direction: a int representing the direction 1 for forward and -1 for reverse
        set_current_player: a int representing the current player
        next_player: a int representing the expected next_player
    """
    uno_deck = Deck()
    uno_game = PlayGame(uno_deck, ["0", "1", "2", "3"])
    uno_game.direction = set_direction
    uno_game.current_player = set_current_player
    uno_game.skip_card_played()

    assert uno_game.next_player() == next_player
