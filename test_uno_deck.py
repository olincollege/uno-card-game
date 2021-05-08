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
