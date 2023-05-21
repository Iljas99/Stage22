# Zebra emulation program
# Page manager
# Stage 22 (Basic task)
# Subject theme: Python Object-Oriented Programming. Send Messages and Code Reuse
# Version: 1.0
# Autor: Ilja
# Date: 10.05.2023


from footplayer import FootballPlayer


class Manager:
    @staticmethod
    def give_golden_ball(players):
        if isinstance(players, (list, tuple)):
            goal = players[0].goal
            assist = players[0].assist
            best_player = players[0]

            for player in players:
                if isinstance(player, FootballPlayer):

                    if goal < int(player.goal):
                        best_player = player
                    elif (goal == player.goal
                          and assist < player.assist):
                        best_player = player

            return best_player

    @staticmethod
    def give_golden_ball02(players):
        if isinstance(players, (list, tuple)):
            result = 3 * players[0].goal + players[0].assist
            goal = players[0].goal
            best_player = players[0]

            for player in players:
                result2 = 3 * int(player.goal) + int(player.assist)
                if isinstance(player, FootballPlayer):

                    if result < result2:
                        best_player = player
                    elif (result == result2
                          and goal < player.goal):
                        best_player = player

            return best_player
