import sys
import random
from enum import Enum


def guess_number(name='PlayerOne'):
    game_count = 0
    player_wins = 0

    def play_guess_number():
        nonlocal name
        nonlocal player_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(
            f"\n{name}, guess which number I'm thinking of... 1, 2, or 3\n\n"
        )

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please must enter 1, 2, or 3")
            return play_guess_number()

        player = int(playerchoice)

        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print(f"\n{name}, you chose {player}.")
        print(f"\nI was thinking about the number {computer}.\n")

        def decide_winner(player, computer):
            nonlocal player_wins

            if player == computer:
                player_wins += 1
                return f"🎉 {name}, you win!"
            else:
                return f"\nSorry, Dave. Better luck next time. 🥲"

        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {str(game_count)}")
        print(f"\n{name}'s wins: {str(player_wins)}")
        print(f"\nYour winning percentage: {player_wins / game_count:.2%}")

        print(f"\nPlay again, {name}?")
        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            play_guess_number()
        else:
            print("\n🎉🎉🎉🎉🎉🎉🎉")
            print("Thanks for playing!\n")
            if __name__ == "__main__":
                sys.exit(f"Bye {name}! ✋")
            else:
                return

    return play_guess_number


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

    guess_number = guess_number(args.name)
    guess_number()
