from functools import reduce
from .game import Game

class RawStateGenerator:
    __ordem__ = [Game.empty, Game.player1, Game.player2]

    def __init__(self):
        self.__state__ = [Game.empty for i in range(9)]
        self.finished = False
        pass

    def __iter__(self):
        return self

    def __next__(self):
        if self.finished:
            raise StopIteration

        self.add(8, [1, 0, 0, 0, 0, 0, 0, 0, 0])

        # voltou tudo p/ o estado inicial então retorna ele e no prox para
        self.finished = reduce(lambda a, b: a and b, [x == self.__ordem__[0] for x in self.__state__], True)

        return self.__state__
        pass

    def add(self, index, amount):

        if index < 0:
            return False

        vem_um = self.add(index - 1, amount)

        amount[index] += 1 if vem_um else 0
        amount[index] += self.__ordem__.index(self.__state__[index])

        self.__state__[index] = self.__ordem__[amount[index] % len(self.__ordem__)]

        return amount[index] >= len(self.__ordem__)
        pass

    pass


class StateGenerator:
    def __init__(self, player):
        self.__currentPLayer__ = player
        self.__game__ = Game()
        self.__raw_generator__ = iter(RawStateGenerator())
        pass

    def __iter__(self):
        return self

    def __next__(self):

        validation = 0 if self.__currentPLayer__ == Game.player1 else 1
        game = self.__game__

        while True:
            state = self.__raw_generator__.__next__()
            game.set_state(state)

            # if the state represents a finished game ignore
            if game.finished():
                continue

            # Number of player1 vs player2 moves on the board
            aggr = sum([1 if x == Game.player1 else -1 if x == Game.player2 else 0 for x in state])
            # any time player1 make a move the board has to have equals amount of moves between p1 and p2 (aggr == 0)
            # on player2 moves case player1 will have one more move than player2 (aggr == 1)
            if aggr != validation:
                continue


            break

            pass

        return state
        pass
