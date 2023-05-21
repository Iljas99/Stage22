# Zebra emulation program
# Page main
# Stage 22 (Basic task)
# Subject theme: Python Object-Oriented Programming. Send Messages and Code Reuse
# Version: 1.0
# Autor: Ilja
# Date: 10.05.2023

from footplayer import FootballPlayer
from manager import Manager


def main():
    leo = FootballPlayer("Leo", "Messi", 910, 450)
    cristiano = FootballPlayer("Cristiano", "Ronaldo", 910, 500)
    alex = FootballPlayer("Alessandro", "Del Piero", 750, 800)
    ivan = FootballPlayer("Ivan", "Ivanov")

    print("List of players:")
    print(leo)
    print(cristiano)
    print(alex)
    print(ivan)
    players = (leo, cristiano, alex, ivan)
    best_player = Manager.give_golden_ball02(players)
    print(f"\nBest player: {best_player}")


if __name__ == "__main__":
    main()
