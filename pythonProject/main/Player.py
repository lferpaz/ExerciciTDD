__authors__='1428612,1564963,1567369'
__group__='411'

class Player:
    def __init__(self, name = None):
        if name is not None:
            self.__playerName__ = name
        else:
            self.__playerName__ = ""

    def __eq__(self, other: str):
        return self.__playerName__ == other.__playerName__

