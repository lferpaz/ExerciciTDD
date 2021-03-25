__authors__='1428612,1564963,1567369'
import pytest
from main.Game import Game
from main.Player import Player


def create_game(player1: Player, player2: Player):
    if player1.__playerName__ == player2.__playerName__:
        player2.__playerName__ = player2.__playerName__ + "_2"
    return Game(player1, player2)


def create_player(name: str):
    return Player(name)

def test_givenGame_WhenNotStarted_ThenLoveAll():
    # ARRANGE
    player1 = create_player("player1")
    player2 = create_player("player2")
    game = create_game(player1, player2)

    # ACT
    result = game.get_score()

    # ASSERT
    assert result == "Love-All"


def test_givenGame_WhenPlayer1WinsFirstPoint_ThenFifteenLove():
    # ARRANGE
    player1 = create_player("player1")
    player2 = create_player("player2")
    game = create_game(player1, player2)
    game.won_point("player1")

    # ACT
    result = game.get_score()

    # ASSERT
    assert result == "Fifteen-Love"


def test_givenGame_WhenPlayer1WinsFirstPoint_AndPlayer2WinsSecondPoint_ThenFifteenAll():
    # ARRANGE
    player1 = create_player("player1")
    player2 = create_player("player2")
    game = create_game(player1, player2)
    game.won_point("player1")
    game.won_point("player2")

    # ACT
    result = game.get_score()

    # ASSERT
    assert result == "Fifteen-All"


def test_givenGame_WhenPlayer1WinsFirstAndThirdPoints_AndPlayer2WinsSecondPoint_ThenThirtyFifteen():
    # ARRANGE
    player1 = create_player("player1")
    player2 = create_player("player2")
    game = create_game(player1, player2)
    game.won_point("player1")
    game.won_point("player2")
    game.won_point("player1")

    # ACT
    result = game.get_score()

    # ASSERT
    assert result == "Thirty-Fifteen"


def test_givenGame_WhenPlayer1WinsFirstAndSecondPoints_ThenThirtyLove():
    # ARRANGE
    player1 = create_player("player1")
    player2 = create_player("player2")
    game = create_game(player1, player2)
    game.won_point("player1")
    game.won_point("player1")

    # ACT
    result = game.get_score()

    # ASSERT
    assert result == "Thirty-Love"


def test_givenGame_WhenPlayer1WinsFirstAndSecondPoints_ThenThirtyLove():
    # ARRANGE
    player1 = create_player("player1")
    player2 = create_player("player2")
    game = create_game(player1, player2)
    game.won_point("player1")
    game.won_point("player1")

    # ACT
    result = game.get_score()

    # ASSERT
    assert result == "Thirty-Love"


def test_givenGame_WhenPlayer1WinsFirstAndSecondAndThirtyPoints_ThenFortyLove():
    # ARRANGE
    player1 = create_player("player1")
    player2 = create_player("player2")
    game = create_game(player1, player2)
    game.won_point("player1")
    game.won_point("player1")
    game.won_point("player1")

    # ACT
    result = game.get_score()

    # ASSERT
    assert result == "Forty-Love"


def test_givenGame_WhenPlayer1WinsFirstAndSecondAndThirtyPointsAndFortyPoints_ThenWinForPlayer1():
    # ARRANGE
    player1 = create_player("player1")
    player2 = create_player("player2")
    game = create_game(player1, player2)
    game.won_point("player1")
    game.won_point("player1")
    game.won_point("player1")
    game.won_point("player1")

    # ACT
    result = game.get_score()

    # ASSERT
    assert result == "Win for player1"


def test_givenGame_WhenPlayer2WinsFirstPoints_ThenLoveFifteen():
    # ARRANGE
    player1 = create_player("player1")
    player2 = create_player("player2")
    game = create_game(player1, player2)
    game.won_point("player2")

    # ACT
    result = game.get_score()

    # ASSERT
    assert result == "Love-Fifteen"


def test_player_nameinit():
    # ARRANGE
    player1 = create_player("best_player")

    # ACT
    result = player1.__playerName__

    # ASSERT
    assert result == "best_player"


def test_player_emptyinit():
    # ARRANGE
    player1 = create_player(None)

    # ACT
    result = player1.__playerName__

    # ASSERT
    assert result == ""


def test_player_eqoperator():
    # ARRANGE
    player1 = create_player("Rafa Nadal")
    player_same_name = create_player("Rafa Nadal")

    # ACT
    result = (player1.__playerName__ == player_same_name.__playerName__)

    # ASSERT
    assert result


def test_game_canCallGetScore():
    # ARRANGE
    game = create_game(create_player("player1"), create_player("player2"))

    # ACT
    result = "error"
    result = game.get_score()

    # ASSERT
    assert result != "error"


def test_game_won_adds1to_player1():
    # ARRANGE
    game = create_game(create_player("player1"), create_player("player2"))
    game.won_point("player1")

    # ACT
    result = game.__points_player1__

    # ASSERT
    assert result == 1


def test_game_init():
    # ARRANGE
    game = create_game(create_player("player1"), create_player("player2"))

    # ACT
    result = game.__points_player1__ == 0
    result2 = game.__points_player2__ == 0
    result3 = (len(game.__combinations__) > 0)

    # ASSERT
    assert (result and result2 and result3)


def test_exploracion_won_point_to_a_won_game():
    # ARRANGE
    game = create_game(create_player("player1"), create_player("player2"))
    game.won_point("player1")
    game.won_point("player1")
    game.won_point("player1")
    game.won_point("player1")
    game.won_point("player1")

    # ACT
    result = game.__points_player1__

    # ASSERT
    assert result == 4


def test_exploracion_player1_diff_from_player2():
    # ARRANGE
    player1 = create_player("player")
    player2 = create_player("player")
    game = create_game(player1, player2)

    # ACTION
    name1 = game.__player1__.__playerName__
    name2 = game.__player2__.__playerName__

    # ASSERT
    assert name1 != name2


def test_create_player():
    # ARRANGE
    p1 = create_player("player1")

    # ACT
    result = isinstance(p1, Player)

    # ASSERT
    assert result


def test_create_game():
    # ARRANGE
    p1 = create_player("player1")
    p2 = create_player("player2")
    g1 = create_game(p1, p2)

    # ACT
    result = isinstance(g1, Game)

    # ASSERT
    assert result

# end of test_tennis_par.py