from random import randrange

class Player:

    def __init__(self, game):
        self.game = game

    def nextMove(self):
        pass

class Human_Player(Player):

    def __init__(self, game):
        super().__init__(game)

    def nextMove(self):
        index = input()
        return int(index)

class Stupid_IA_Player(Player):
    def __init__(self, game):
        self.game = game

    def nextMove(self):
        rand = randrange(0, 9)
        while not self.game.empty_pos(rand):
            rand = randrange(0, 9)
        return rand