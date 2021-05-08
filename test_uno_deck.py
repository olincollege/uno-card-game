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

#create test



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
    Checks that the average image finder returns an average of all the images in the list
    using our first color averaging method.

    Args:
        password: A string representing the password to check.
        passes_check: A bool representing the expected output of the checker.
    """
    uno_card = Card(color,rank)
    assert str(uno_card) == resulting_card


@pytest.mark.parametrize("resulting_card_count, resulting_middle_count", [
    # Checks that the deck creates 112 cards and starts the middle pile at 0 cards
    (112, 0)
])
def test_deck(resulting_card_count, resulting_middle_count):
    """
    Checks that the average image finder returns an average of all the images in the list
    using our second color averaging method.

    Args:
        image_list: a list representing the images to average.
        resulting_image: a image representing the expected resulting average image.
    """
    uno_deck = Deck()
    assert (len(uno_deck.cards), len(uno_deck.middle)) == \
        (resulting_card_count, resulting_middle_count)

def test_shuffle():
    """
    Checks that the average image finder returns an average of all the images in the list
    using our second color averaging method.

    Args:
        image_list: a list representing the images to average.
        resulting_image: a image representing the expected resulting average image.
    """
    uno_deck = Deck()
    uno_cards = [] + uno_deck.cards
    uno_deck.shuffle()
    shuffled_uno_cards = [] +uno_deck.cards
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
    Checks that the average image finder returns an average of all the images in the list
    using our second color averaging method.

    Args:
        image_list: a list representing the images to average.
        resulting_image: a image representing the expected resulting average image.
    """
    shuffled_uno_deck = Deck()
    shuffled_uno_deck.shuffle()
    drawn_cards = shuffled_uno_deck.draw(number_cards_pulled)
    

    assert (len(shuffled_uno_deck.cards), len(drawn_cards)) == \
        (resulting_deck_count, resulting_draw_count)

@pytest.mark.parametrize("card, is_match", [
    # Checks that the draw of 112 cards results in proper values
    (Card("Red",0), True),
    # Check a draw of 0
    (Card("Red",1), True),
    # Check a draw of 1
    (Card("Blue",0), True),
    # Check a draw of 4 
    (Card("Blue",1), False),
    (Card("Red",10), True),
    (Card("Blue",10), False),
    (Card("Wild",13), True),
    (Card("Wild",14), True),
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
    # Checks that the draw of 112 cards results in proper values
    (Card("Red",0), False),
    # Check a draw of 0
    (Card("Blue",1), False),
    # Check a draw of 1
    (Card("Yellow",10), True),
    # Check a draw of 4 
    (Card("Green",11), True),
    (Card("Red",12), True),
    (Card("Wild",13), True),
    (Card("Wild",14), True),
])
def test_deck_check_action(card, is_action):
    """
    Checks that the average image finder returns an average of all the images in the list
    using our second color averaging method.

    Args:
        image_list: a list representing the images to average.
        resulting_image: a image representing the expected resulting average image.
    """
    uno_deck = Deck()
    assert uno_deck.check_action(card) == is_action

@pytest.mark.parametrize("number_cards_pulled, number_cards_in_hand", [
    # Checks that the draw of 112 cards results in proper values
    (2,9),
    # Check a draw of 0
    (0,7),
    # Check a draw of 1
    (1,8),
    # Check a draw of 4 
    (13,20),
])
def test_player_draw(number_cards_pulled, number_cards_in_hand):
    """
    Checks that the average image finder returns an average of all the images in the list
    using our second color averaging method.

    Args:
        image_list: a list representing the images to average.
        resulting_image: a image representing the expected resulting average image.
    """
    uno_deck = Deck()
    uno_player = Player(uno_deck,"name")
    uno_player.draw(number_cards_pulled)
    assert len(uno_player.hand)== number_cards_in_hand