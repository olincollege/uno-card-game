"""
Uno game view.
"""
from abc import ABC, abstractmethod


class UnoView(ABC):
    """
    Abstract base class representing a view of a Uno game.

    Attributes:
        _game: A Uno game instance representing the uno game
                to display.
    """

    def __init__(self, game):
        """
        Create a new view of a uno game.

        Args:
            board: A Uno game instance representing the uno game
                to display.
        """
        self._game = game

    @property
    def game(self):
        """
        Return the Uno game instance being represented by this view.
        """
        return self._game

    @abstractmethod
    def display(self):
        """
        Display a representation of the current state of the game
        """
        pass


class TextView(UnoView):
    """
    Text-based view of a Uno game.
    """

    def display(self):
        """
        Display a representation of the current state of the game.
        """
        for player in self.game.player_list:
            print(f"{player._name}:\n\t\t12345")
            print(("\t\t"+u'\u258a'*len(player._hand))+"\n")
