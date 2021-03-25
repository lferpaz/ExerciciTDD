__authors__='1428612,1564963,1567369'
__group__='411'

from main.Player import Player

class Game:
    def __init__(self, player_1: Player, player_2: Player):
        self.__player1__ = player_1
        self.__player2__ = player_2
        self.__points_player1__ = 0
        self.__points_player2__ = 0
        self.__combinations__ = [["Love-All", "Love-Fifteen", "Love-Thirty", "Love-Forty", "Win for player2"],
                           ["Fifteen-Love", "Fifteen-All", "Fifteen-Thirty", "Fifteen-Forty", "Win for player2"],
                           ["Thirty-Love", "Thirty-Fifteen", "Thirty-All", "Thirty-Forty", "Win for player2"],
                           ["Forty-Love", "Forty-Fifteen", "Forty-Thirty", "Deuce", "Advantage player2"],
                           ["Win for player1", "Win for player1", "Win for player1", "Advantage player1", "Deuce"]]

    def get_score(self):
        if (self.__points_player1__ + self.__points_player2__) <= 6:
            return self.__combinations__[self.__points_player1__][self.__points_player2__]
        else:
            if self.__points_player1__ == self.__points_player2__:
                return "Deuce"
            elif (self.__points_player1__ - self.__points_player2__) == 1:
                return "Advantage player1"
            elif (self.__points_player1__ - self.__points_player2__) == -1:
                return "Advantage player2"
            elif (self.__points_player1__ - self.__points_player2__) == 2:
                return "Win for player1"
            elif (self.__points_player1__ - self.__points_player2__) == -2:
                return "Win for player2"


    def won_point(self, player_obj: str):
        if (self.get_score() == "Win for player1"):
            print("Could not won_point--> GAME is won for player1")
        elif (self.get_score() == "Win for player2"):
            print("Could not won_point--> GAME is won for player2")
        else:
            if self.__player1__.__playerName__ == player_obj:
                self.__points_player1__ = self.__points_player1__ + 1
            else:
                self.__points_player2__ = self.__points_player2__ + 1