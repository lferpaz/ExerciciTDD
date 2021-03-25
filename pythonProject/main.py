__authors__='1428612,1564963,1567369'
from test.test_tennis_par import *

def tests_integracion():
    test_givenGame_WhenPlayer1WinsFirstPoint_ThenFifteenLove()
    test_givenGame_WhenPlayer1WinsFirstPoint_AndPlayer2WinsSecondPoint_ThenFifteenAll()
    test_givenGame_WhenPlayer1WinsFirstAndThirdPoints_AndPlayer2WinsSecondPoint_ThenThirtyFifteen()
    test_givenGame_WhenPlayer1WinsFirstAndSecondPoints_ThenThirtyLove()
    test_givenGame_WhenPlayer1WinsFirstAndSecondAndThirtyPoints_ThenFortyLove()
    test_givenGame_WhenPlayer1WinsFirstAndSecondAndThirtyPointsAndFortyPoints_ThenWinForPlayer1()
    test_givenGame_WhenPlayer2WinsFirstPoints_ThenLoveFifteen()

def tests_unitarios_player():
    test_player_nameinit()
    test_player_emptyinit()
    test_player_eqoperator()

def tests_unitarios_game():
    test_givenGame_WhenNotStarted_ThenLoveAll()
    test_game_canCallGetScore()
    test_game_init()
    test_game_won_adds1to_player1()

def tests_exploracion():
    test_exploracion_won_point_to_a_won_game()
    test_exploracion_player1_diff_from_player2()
    test_create_player()
    test_create_game()

if __name__ == '__main__':
    # tests game
    tests_integracion()
    tests_unitarios_game()
    tests_unitarios_player()
    tests_exploracion()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
