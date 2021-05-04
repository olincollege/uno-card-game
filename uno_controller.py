"""
Uno controller.
"""
from abc import ABC, abstractmethod


class UnoController(ABC):
    """
    Abstract base class representing a controller for a tic-tac-toe game.

    Attributes:
        _board: A Uno instance representing the tic-tac-toe game to
            send moves to.
    """

    def __init__(self, board):
        """
        Create a new controller for a tic-tac-toe game.

        Args:
            board: A TicTacToeBoard instance representing the tic-tac-toe game
                to send moves to.
        """
        self._board = board

    @property
    def board(self):
        """
        Return the TicTacToeBoard instance this controller interacts with.
        """
        return self._board

    @abstractmethod
    def move(self):
        """
        Make a valid move in the current board.
        """
        pass


class TextController(TicTacToeController):
    """
    Text-based controller for tic-tac-toe that takes user input representing
    board coordinates.
    """

    def move(self):
        """
        Obtain text input from the user to make a move in the current board,
        repeating the process until a valid move is made.
        """
        move = input("Input row/column numbers for your move, separated by a"
                     " space (e.g., \"0 0\"): ")
        try:
            numbers = move.strip().split()
            row = int(numbers[0])
            col = int(numbers[1])
            if row < 0 or col < 0:
                raise ValueError
            self._board.mark(row, col)
        except (IndexError, ValueError):
            print(f"Error with input '{move}'. Please try again.")
            self.move()
