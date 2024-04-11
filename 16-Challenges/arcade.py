
import sys
from rps import rps
from guess_number import guess_number


def arcade(name="PlayerOne"):
    def play_arcade():

        nonlocal name

        playerchoice = input(
            f"\n\nPlease choose a game:\n1 = Rock Paper Scissors\n2 = Guess the Number\n\nOr press \"x\" to exit the Arcade\n\n"
        )

        if playerchoice not in ['1', '2', 'x']:
            print(f"\n\n{name}, please must enter 1, 2, or x")
            return play_arcade()

        player = playerchoice

        if player == '1':
            rps(name)()
            play_arcade()
        elif player == '2':
            guess_number(name)()
            play_arcade()
        else:
            print(f"\nSee you next time!\nBye {name}! 👋\n")
            return sys.exit()


    return play_arcade


if __name__ == "__main__":
    import argparse


    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    print(f"\n{args.name}, welcome to the Arcade! 🤖")

    arcade = arcade(args.name)
    arcade()
