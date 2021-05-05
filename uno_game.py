"""
Main program to set up and run a uno game.
"""
from uno_deck import Deck, PlayGame
from uno_view import TextView
from uno_controller import TextController


def main():
    """
    Play a game of uno
    """
    # Set up the MVC components.
    continue_game = "y"
    while continue_game == "y":
        uno_set = Deck()
        uno_controller = TextController(uno_set)
        names = uno_controller.start()
        uno_set.game_start()
        uno_game = PlayGame(uno_set, names)
        view = TextView(uno_game)
        while not uno_game.check_win():
            view.display()
            uno_game.play()
        for player in uno_game.player_list:
            if player.check_empty():
                uno_game.win_message(player)
                continue_game = input("Do you want to continue play again? y/n: ")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
