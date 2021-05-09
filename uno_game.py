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
    print("Welcome to Uno!\n \
        Here are the rules:\n \
        1. Match the card in the middle by either color or number\n \
        2. Watch out for action cards! Plus Two, Skip, Reverse, and Wild Cards\n \
        3. If you are at one card and the game prompts you with: \n\t\"Hit enter once you are finished with your turn\"\n \
        Please type \"Uno!\" or else you will get extra cards\n \
        4. Do not look at other player cards!\n\n")
    continue_game = "y"
    while continue_game == "y":
        uno_set = Deck()
        uno_controller = TextController(uno_set)
        names = uno_controller.start()
        uno_game = PlayGame(uno_set, names)
        uno_set.game_start()
        view = TextView(uno_game)
        while not uno_game.check_win():
            view.display()
            uno_game.play()
        for player in uno_game.player_list:
            if player.check_empty():
                uno_game.win_message(player)
                continue_game = input(
                    "Do you want to continue play again? y/n: ")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
