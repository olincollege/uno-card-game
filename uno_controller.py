"""
Uno controller.
"""
from abc import ABC, abstractmethod


class UnoController(ABC):
    """
    Abstract base class representing a controller for a Uno game.

    Attributes:
        _deck: A Uno instance representing the Uno game to
            send moves to.
    """

    def __init__(self, deck):
        """
        Create a new controller of a uno game.

        Args:
            deck: A Uno game instance representing the uno game
                to control.
        """
        self._deck = deck

    @property
    def game(self):
        """
        Return the Uno game instance being controlled.
        """
        return self._deck

    @abstractmethod
    def start(self):
        """
        Send the start singal to the game.
        """


class TextController(UnoController):
    """
    Text-based controller for Uno Game that takes user input representing
    player names.
    """

    def start(self):
        """
        Obtain text input from the user to give names to the players and start the game.
        """
        names = input("Input four players names with a single space in between " +
                      "(e.g., \"name1 name2 ...\"): ").split()
        try:
            if len(names) != 4:
                raise ValueError
            return names
        except (IndexError, ValueError):
            print(f"Error with input '{names}'. Please try again.")
            self.start()
