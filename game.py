from board import *
game = Board()


class BusyCoordException(Exception):
    """
    Class for mistake representation.
    Mistake raises if the user wants to go on the busy coordinate.
    """
    pass


def user_move():
    try:
        a = input("Type the first coordinate (0 - 2): ")
        b = input("Type the second coordinate (0 - 2): ")
        if not game.make_move((int(a), int(b))):

            raise BusyCoordException

    except (ValueError, IndexError):
        print("Please, write coordinate in range from 0 to 2!")
        user_move()

    except BusyCoordException:
        print("Please, choose free coordinates!")
        user_move()


def play():
    while not game.has_winner():
        user_move()

        if game.has_winner() == 2:
            print(game)
            print("Draw!")
            break
        elif game.has_winner():
            print(game)
            print("You won!")
            break

        game.make_random_move()
        if game.has_winner() == 2:
            print(game)
            print("You lost...")
            break
        elif game.has_winner():
            print("Draw!")
            break

        print(game)


play()
